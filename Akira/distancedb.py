import sys
from sqlalchemy import Column,String,Date,Integer,VARCHAR,DECIMAL
from database import Base
from database import ENGINE
from database import session



# テーブル名とカラムの宣言
class Station(Base):
    __tablename__='stations'
    seq = Column('seq',Integer,primary_key=True)
    name = Column("name",VARCHAR(20))
    kilo = Column("kiro",DECIMAL(6,2))

def main(args):
    Base.metadata.create_all(bind = ENGINE)
    

if __name__=="__main__":
    main(sys.argv)

    # 引数取得
    args = sys.argv
    start_station_name = args[1]
    finish_station_name = args[2]

    # 引数で受け取った駅名と同じ行の距離を取得
    station_name_list = session.query(Station).all()
    for list in station_name_list:
        if list.name == start_station_name:
            start_station_kiro = list.kilo

        if list.name == finish_station_name:
            finish_station_kiro = list.kilo

    # ２つの距離の差を表示
    print(abs(start_station_kiro - finish_station_kiro))


