import sys
from sqlalchemy import Column,Integer,VARCHAR,DECIMAL,Date
from database import Base
from database import ENGINE
from database import session



class Station(Base):
    __tablename__='transport'
    date = Column('date',Date,primary_key=True)
    seq = Column("seq",Integer)
    departure = Column("departuer",VARCHAR(20))
    
def main(args):

    Base.metadata.create_all(bind = ENGINE)
    

if __name__=="__main__":
    main(sys.argv)

    args = sys.argv
    start_station_name = args[1]
    finish_station_name = args[2]

    station_name_list = session.query(Station).all()
    for list in station_name_list:
        if list.name == start_station_name:
            start_station_kiro = list.kilo

        if list.name == finish_station_name:
            finish_station_kiro = list.kilo

    print(abs(start_station_kiro - finish_station_kiro))


