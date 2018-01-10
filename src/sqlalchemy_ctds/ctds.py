'''
.. dialect:: mssql+ctds
    :name: ctds
    :dbapi: ctds
    :connectstring: mssql+ctds://<username>:<password>@<host>/
    :url: https://zillow.github.io/ctds
'''
import re

from sqlalchemy.dialects.mssql.base import MSDialect, BINARY, VARBINARY
from sqlalchemy import types as sqltypes, util


class _Binary_ctds(object):
    def bind_processor(self, dialect):
        if dialect.dbapi is None:
            return None

        return dialect.dbapi.Binary

class _VARBINARY_ctds(_Binary_ctds, VARBINARY):
    pass


class _BINARY_ctds(_Binary_ctds, BINARY):
    pass


class MSDialect_ctds(MSDialect):
    driver = 'ctds'
    convert_unicode = False
    supports_sane_multi_rowcount = False
    supports_sane_rowcount_returning = False
    supports_sane_rowcount = False
    supports_native_decimal = True
    supports_unicode_statements = True
    supports_unicode_binds = True
    returns_unicode_strings = True
    paramstyle = 'named'
    default_paramstyle = 'named'

    colspecs = util.update_copy(
        MSDialect.colspecs,
        {
            BINARY: _BINARY_ctds,
            VARBINARY: _VARBINARY_ctds,
            sqltypes.VARBINARY: _VARBINARY_ctds,
            sqltypes.LargeBinary: _VARBINARY_ctds,
        }
    )

    @classmethod
    def dbapi(cls):
        module = __import__('ctds')

        # Setting this won't change the default in ctds, but it is used by sqlalchemy
        # and hence necessary.
        module.paramstyle = cls.paramstyle
        return module

    def _get_server_version_info(self, connection):
        version = connection.scalar('SELECT @@VERSION')
        m = re.match(
            r'Microsoft .*? - (\d+).(\d+).(\d+).(\d+)', version)
        if m:
            return tuple(int(x) for x in m.group(1, 2, 3, 4))
        else:
            return None

    def create_connect_args(self, url):
        opts = url.translate_connect_args(username='user')
        opts.update(url.query)
        opts.update(
            {
                'autocommit': False,
                'paramstyle': self.paramstyle,
            }
        )
        server = opts.pop('host', None)
        return [[server], opts]

    def is_disconnect(self, e, connection, cursor):
        for msg in (
            'Adaptive Server connection timed out',
        ):
            if msg in str(e):
                return True
        else:
            return False

    def set_isolation_level(self, connection, level):
        if level == 'AUTOCOMMIT':
            connection.autocommit = True
        else:
            connection.autocommit = False
            super(MSDialect_ctds, self).set_isolation_level(connection, level)


dialect = MSDialect_ctds
