from database import session
from tables import Stations
import sys
args = sys.argv

departure_station = (args[1])
arrival_station = (args[2])

stations=session.query(Stations).filter(Stations.name.in_([input_from, input_to])).all()

distance = map[args[2]] - map[args[1]]
print(abs(round(distance, 2)), end="")
