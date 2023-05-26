import sys

# 引数の取得
args = sys.argv
meter = map(int(args[1]))

# 距離が1500を超えるか判断
if meter > 1500: # 1500を超える場合の値段
    orver_meter = meter -1500
    orver_meter_money = (orver_meter%344 + 1) * 98
    pay = 630 + orver_meter_money

else : pay = 630 # 1500を超えない場合の値段

print(pay, end="")