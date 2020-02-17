from sqlalchemy import create_engine
from sqlalchemy import Column, Float, ForeignKey, Index, Integer, Table, Text, text, and_
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from datetime import datetime
from project_alphavantage.config.base import (
    BASE_DIR
)

SQLITE = 'sqlite'
Base = declarative_base()
metadata = Base.metadata


class Stock(Base):
    __tablename__ = 'stock'

    id = Column(Integer, primary_key=True)
    symbol = Column(Text, nullable=False)
    name = Column(Text, nullable=False)
    active = Column(Integer, nullable=False, server_default=text("1"))

    @staticmethod
    def get_all_active_stock():
        Session = sessionmaker(bind=AlphaVantageDB(dbtype='sqlite', dbname='alphavantage').db_engine)
        session = Session()
        actives_stocks = session.query(Stock).filter(Stock.active == True).all()
        session.close()
        return actives_stocks


class StockImport(Base):
    __tablename__ = 'stock_import'
    __table_args__ = (
        Index('stock_imported_date_idx', 'stock_id', 'date', unique=True),
    )
    id = Column(Integer, primary_key=True)
    date = Column(Text, nullable=False)
    close = Column(Float, nullable=False, server_default=text("0"))
    stock_id = Column(ForeignKey('stock.id'), nullable=False)
    stock = relationship('Stock')
    
    @staticmethod
    def save_or_update_stock_imports(date: str, close: float, stock: Stock):
        Session = sessionmaker(bind=AlphaVantageDB(dbtype='sqlite', dbname='alphavantage').db_engine)        
        session = Session()
        stock_import = session.query(StockImport).filter(and_(StockImport.date == date, StockImport.stock == stock))
        try:
            if stock_import.one():
                stock_import.one().close = close            
        except NoResultFound:
            session.add(StockImport(date=date, close=close, stock=stock))
        session.commit()
        session.close()


class AlphaVantageDB(object):
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
        else:
            print("DBType is not found in DB_ENGINE")
