# モジュールをインポート
import sys

# 引数を変数へ代入
args = sys.argv
karaage = int(args[1])
curry = int(args[2])

# 品目ごとのトータル計算
karaage_pay = karaage * 760
curry_pay = curry * 850

# 1日のトータル計算
total = karaage_pay + curry_pay

# 出力
print(total, end="")