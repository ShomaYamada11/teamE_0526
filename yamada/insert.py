from datetime import date
from database import session #1.データベースへの接続
from stationtable import Stations #2.テーブル定義

#登録するデータの編集
holiday = Stations(
    seq = 1,
    name = "東京",
    kilo = 0.00
)
session.add(holiday)
session.commit()

holiday = Stations(
    seq =2,
    name = "品川",
    kilo = 6.78
)
session.add(holiday)
session.commit()

holiday = Stations(
    seq = 3,
    name = "新横浜",
    kilo = 25.54
)
session.add(holiday)
session.commit()

holiday = Stations(
    seq = 4,
    name = "名古屋",
    kilo = 342.02
)
session.add(holiday)
session.commit()

holiday = Stations(
    seq = 5,
    name = "京都",
    kilo = 476.31
)
session.add(holiday)
session.commit()

holiday = Stations(
    seq = 6,
    name = "新大阪",
    kilo = 515.35
)
session.add(holiday)
session.commit()