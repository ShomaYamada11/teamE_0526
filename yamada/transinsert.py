import sys
from sqlalchemy import Column, Integer, Date, VARCHAR
from database import Base
from database import ENGINE
from database import session
from datetime import date

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

    args = sys.argv

    #引数を変数に代入
    today = args[1]
    #年月日をスライス
    year = today[:4]
    month = today[4:6]
    day = today[6:]

    num = int(args[2])
    departure_station = args[3]
    arrival_station = args[4]
    via_line = args[5]
    money = int(args[6])

    #既に同じ日、連番のものがあるかチェック
    existing_data = 0
    transport_list = session.query(Transport).all()
    for transports in transport_list:
        if transports.date == date(int(year),int(month),int(day)) and transports.seq == num:
            existing_data = 1
            break

    #ある場合とない場合のパターン分け
    if existing_data != 0:
        print("error:交通費精算テーブルにデータを登録できませんでした")

    else:
        #登録するデータ
        data = Transport(
            date = date(int(year),int(month),int(day)),
            seq = num,
            departure = departure_station,
            arrival = arrival_station,
            via = via_line,
            amount = money
        )

        #データ登録
        session.add(data)
        session.commit()

        #データ登録完了を通知
        print("交通費精算テーブルにデータを登録しました")