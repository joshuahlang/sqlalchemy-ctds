__version__ = "0.1.0"

from sqlalchemy.dialects import registry

registry.register("mssql.ctds", "sqlalchemy_ctds.ctds", "MSDialect_ctds")
