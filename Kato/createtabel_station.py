from sqlalchemy import *
from sqlalchemy.orm import * 
from sqlalchemy.ext.declarative import declarative_base
import os

DATABASE = "mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8".format(**{
        "user": os.getenv("DB_USESR", "root"),
        "password": os.getenv("DB_PASSWORD", "mysql"),
        "host": os.getenv("DB_HOST", "localhost"),
        "database": os.getenv("DB_DATABASE", "ENSHU")
    })
ENGINE = create_engine(
    DATABASE,
    encoding = "utf-8",
    echo = True
)

session = scoped_session(
    sessionmaker(
        autocommit = False,
        autoflush = False,
        bind = ENGINE
    )
)

Base = declarative_base()
Base.query = session.query_property()
import sys
from sqlalchemy import Column, INTEGER, VARCHAR, DECIMAL

class STATION(Base):
    __tablename__ = 'station'
    seq = Column('seq', INTEGER, primary_key = True)
    name = Column('name', VARCHAR(20))
    kilo = Column('kilo', DECIMAL(6,2))

def main(args):
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main(sys.argv)
