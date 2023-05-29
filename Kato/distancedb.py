import sys
args = sys.argv
import getstation

station = [args[1], args[2]]    #駅名をリストにする

distance = getstation.get_station(station)  #距離を計算する関数を呼び出す

print(distance, end="")     #結果を表示

