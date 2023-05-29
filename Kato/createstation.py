from createtabel_station import session
from createtabel_station import STATION

#station = session.query(STATION).filter_by(seq = 6).delete()


station = STATION(
    #seq = 1, name1 = "東京", st_kilo = 0.00,
    #seq = 2, name = "品川", kilo = 6.78
    #seq = 3, name = "新横浜", kilo = 25.54
    #seq = 4, name = "名古屋", kilo = 342.02,
    #seq = 5, name = "京都", kilo = 476.31
    seq = 6, name = "新大阪", kilo = 515.35
)

session.add(station)

session.commit()