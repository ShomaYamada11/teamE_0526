from createtabel_station import session
from createtabel_station import STATION

#データベースから距離を取得し、駅間の距離を計算する関数を定義
def get_station(station):
    distance = []   #距離を取得するリストを定義
    distance.append(session.query(STATION.kilo)\
                    .filter_by(name = station[0]).all())     #距離を取得
    print(distance)
    distance[0] = distance[0][0][0]                          #リストインリストの解消
    distance.append(session.query(STATION.kilo)\
                    .filter_by(name = station[1]).all())     #距離を取得
    distance[1] = distance[1][0][0]                          #リストインリストの解消
    kilo = abs(distance[0] - distance[1])                    #距離を計算
    
    return kilo     #計算した距離を返す