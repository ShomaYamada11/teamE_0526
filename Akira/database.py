# import
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
import os

# mysqlのDB設定
DATABASE = "mysql+pymysql://{user}:{passward}@{host}/{database}?charset=utf8".format(**{
    "user":os.getenv("DB_USER", "root"),
    "passward": os.getenv("DB_PASWORD", "mysql"),
    "host": os.getenv("DB_HOST", "localhost"),
    "database": os.getenv("DB_DATABASE", "ENSHU",)
})

ENGINE = create_engine(
    DATABASE,
    encoding = "utf-8",
    echo=True
)

# Session
session = scoped_session(
    sessionmaker(
        autocommit = False,
        autoflush = False,
        bind = ENGINE
    )
)

Base = declarative_base()
Base.query = session.query_property()

