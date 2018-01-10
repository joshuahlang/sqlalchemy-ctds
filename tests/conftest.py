from sqlalchemy.dialects import registry

registry.register('mssql.ctds', 'sqlalchemy_ctds.ctds', 'MSDialect_ctds')


from sqlalchemy.testing.plugin.pytestplugin import *
