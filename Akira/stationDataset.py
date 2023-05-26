from database import session
from distancedb import Station


station = Station(
    seq = 1,
    name = "東京",
    kilo = 0.00
        )
session.add(station)
session.commit()

station = Station(
    seq = 2,
    name = "品川",
    kilo = 6.78
        )
session.add(station)
session.commit()

station = Station(
    seq = 3,
    name = "新横浜",
    kilo = 25.54
        )
session.add(station)
session.commit()

station = Station(
    seq = 4,
    name = "名古屋",
    kilo = 342.02
        )
session.add(station)
session.commit()

station = Station(
    seq = 5,
    name = "京都",
    kilo = 476.31
        )
session.add(station)
session.commit()

station = Station(
    seq = 6,
    name = "新大阪",
    kilo = 515.35
        )
session.add(station)
session.commit()




