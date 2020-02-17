from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Boolean, String 
from project_alphavantage.config.base import (
    BASE_DIR
)

SQLITE = 'sqlite'

class AlphaVantage:
    """
    A class responsible to connect AlphaVantage database and make operations
    ...
    Attr
    db_engine: Engine
    """
    # http://docs.sqlalchemy.org/en/latest/core/engines.html
    DB_ENGINE = {
        SQLITE: 'sqlite:///{DB_PATH}/{DB}'
    }

    # Main DB Connection Ref Obj
    db_engine = None
    def __init__(self, dbtype, dbname='', dbpath=BASE_DIR):
        dbtype = dbtype.lower()
        if dbtype in self.DB_ENGINE.keys():
            engine_url = self.DB_ENGINE[dbtype].format(DB=dbname, DB_PATH=dbpath)
            self.db_engine = create_engine(engine_url)
            print(self.db_engine)
            print(engine_url)
        else:
            print("DBType is not found in DB_ENGINE")
    
    # Function responsible to execute queries
    def execute_query(self, query=''):
        if query == '' : return        
        with self.db_engine.connect() as connection:
            try:
                connection.execute(query)
            except Exception as e:
                print(e)

