import sys
args = sys.argv

distance = int(args[1])  #乗車距離の値を受け取る
fee = 630   #初乗り料金

if distance > 1500:     #初乗り料金を超えた場合
    if (distance - 1500) % 344 == 0:    #料金切り替えの境目の時
        count = int((distance - 1500) / 344)
    else:
        count = int((distance - 1500) / 344) + 1
    fee +=  count * 98      #料金を計算

print(fee, end="")  #料金を出力