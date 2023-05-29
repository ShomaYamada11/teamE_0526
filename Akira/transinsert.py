import sys
from sqlalchemy import Column,Integer,VARCHAR,DECIMAL,Date
from database import Base
from database import ENGINE
from database import session
from datetime import date,datetime



# テーブル名とカラムの要素を定義
class Transport(Base):
    __tablename__='transport'
    date = Column('date',Date)
    seq = Column("seq",Integer,primary_key=True)
    departure = Column("departuer",VARCHAR(20))
    arrival = Column("arrival", VARCHAR(20))
    via = Column("via",VARCHAR(40) )
    amount = Column("amount", Integer)
    
def main(args):

    Base.metadata.create_all(bind = ENGINE)
    


# メインの処理
if __name__=="__main__":
    main(sys.argv)

    # 引数の取得
    args = sys.argv
    input_stationdata = list(map(str,args[1:]))

    # ８桁をdate型に変更
    dt = datetime.strptime(input_stationdata[0], "%Y%m%d")

    # 想定の処理（すべての要素に値いを代入し登録）
    try:
        transport = Transport(
            date = dt,
            seq = input_stationdata[1],
            departure = input_stationdata[2],
            arrival = input_stationdata[3],
            via = input_stationdata[4],
            amount = input_stationdata[5],
        )
        session.add(transport)
        session.commit()
        print("交通費テーブルにデータを登録できました")
    
    # データの代入がうまくいかなかったときの処理
    except:
        print("error:交通費精算テーブルにデータを登録できませんでした")




