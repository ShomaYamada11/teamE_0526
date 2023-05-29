from datetime import datetime
from database import session # データベースへの接続
from tables import Transport
import sys
args = sys.argv

try:   
    transport = Transport(
        date = datetime.strptime(str(args[1]), "%Y%m%d"),
        seq = int(args[2]),
        departure = str(args[3]),
        arrival = str(args[4]),
        via = str(args[5]),
        amount = int(args[6])
    )

    session.add(transport)
    session.commit()
    print("交通費精算テーブルにデータを登録しました", end="")
except:
    print("error:交通費精算テーブルにデータを登録できませんでした")

