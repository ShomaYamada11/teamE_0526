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
args = sys.argv
from sqlalchemy import Column, DATE, INTEGER, VARCHAR

class Transport(Base):
    __tablename__ = 'transport'
    date = Column('data', DATE, primary_key = True)
    seq = Column('seq', INTEGER, primary_key = True)
    departure = Column('departure', VARCHAR(20))
    arrival = Column('arrival', VARCHAR(20))
    via = Column('via', VARCHAR(40))
    amount = Column('kilo', INTEGER)

def main(args):
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main(sys.argv)