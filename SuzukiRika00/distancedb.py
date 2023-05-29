from database import session
from tables import Stations
import sys
args = sys.argv

departure_station = (args[1])
arrival_station = (args[2])

stations=session.query(Stations).filter(Stations.name.in_([departure_station, arrival_station])).all()
#ここまでやった途中
#distance = map[args[2]] - map[args[1]]
distance = stations[0].kilo - stations[1].kilo

print(abs(round(distance, 2)), end="")
