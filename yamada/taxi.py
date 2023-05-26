import sys
args = sys.argv

#引数を変数に代入
distance = int(args[1])

#変数fareに初乗り料金を代入
fare = 630

if distance > 1500: #距離が1500mを超える場合追加料金計算
    distance = distance - 1500
    add = distance // 344
    fare = fare + 98 * (add + 1)

#料金表示
print(fare, end="")
