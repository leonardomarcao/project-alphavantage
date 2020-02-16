from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Boolean, String 
from project_alphavantage.config.base import (
    DATABASE_PATH
)

class AlphaVantage:
    # http://docs.sqlalchemy.org/en/latest/core/engines.html
    DB_ENGINE = {
        SQLITE: f'sqlite:///{DATABASE_PATH}'
    }

    # Main DB Connection Ref Obj
    db_engine = None
    def __init__(self, dbtype, username='', password='', dbname=''):
        dbtype = dbtype.lower()
        if dbtype in self.DB_ENGINE.keys():
            engine_url = self.DB_ENGINE[dbtype].format(DB=dbname)
            self.db_engine = create_engine(engine_url)
            print(self.db_engine)
        else:
            print("DBType is not found in DB_ENGINE")


