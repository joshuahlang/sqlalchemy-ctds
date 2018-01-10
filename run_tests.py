from sqlalchemy.dialects import registry

registry.register('mssql.ctds', 'sqlalchemy_ctds.pyodbc', 'MSDialect_ctds')

from sqlalchemy.testing import runner

runner.main()
