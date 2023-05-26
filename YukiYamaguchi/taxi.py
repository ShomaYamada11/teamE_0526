# モジュールをインポート
import sys

# 引数を変数へ代入
args = sys.argv
distance = int(args[1])

# 運賃計算
if distance <= 1500: # 1500m以下の場合
    fee = 630
elif distance - 1500 < 344:
    fee = 728
else: 
    extra_far = round((distance - 1500) / 344) * 98
    fee = 630 + extra_far

print(fee, end="")