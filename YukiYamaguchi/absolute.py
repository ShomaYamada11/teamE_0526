# モジュールをインポート
import sys

# 引数を変数へ代入
args = sys.argv
num = int(args[1])

# abs()関数で絶対値を換算し出力
print(num, end="")
print(" ", end="")
print(abs(num), end="")
