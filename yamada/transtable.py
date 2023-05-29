from sqlalchemy import Column, Integer, Date, VARCHAR
from database import Base
from database import ENGINE
import sys

#テーブル:Transportの定義
class Transport(Base):
    __tablename__ = 'transport'
    date = Column('date', Date, primary_key = True)
    seq = Column('seq', Integer, primary_key = True)
    departure = Column('departure', VARCHAR(20))
    arrival = Column('arrival', VARCHAR(20))
    via = Column('via', VARCHAR(40))
    amount = Column('amount', Integer)

def main(args):
    """メイン関数"""
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main(sys.argv)