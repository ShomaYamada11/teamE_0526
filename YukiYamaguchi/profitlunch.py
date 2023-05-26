# モジュールをインポート
import sys

# 引数を変数へ代入
args = sys.argv
karaage = int(args[1])
curry = int(args[2])

# 品目ごとの売り上げ
karaage_pay = karaage * 760
curry_pay = curry * 850
sales = karaage_pay + curry_pay

# 原価計算
karaage_cost = round(karaage_pay * 0.323)
curry_cost = round(curry_pay * 0.284)
cost = karaage_cost + curry_cost

# 粗利計算
profit = sales - cost

# 結果出力
print("売上高：" + str(sales) + "、"+ "原価：" + str(cost) + "、"+ "粗利：" + str(profit), end="")


