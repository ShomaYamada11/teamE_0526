from database import session
from stationtable import Stations
import sys

args = sys.argv

#引数を変数に代入
departure_station = args[1]
arrival_station = args[2]


station_list = session.query(Stations).all()
for list in station_list:
    if list.name == departure_station:
            start_station_kiro = list.kilo
    if list.name == arrival_station:
        finish_station_kiro = list.kilo

print(abs(start_station_kiro - finish_station_kiro))
