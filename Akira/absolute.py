import sys

# 引数をint型のリストに格納
args = sys.argv
num = list(map(int, sys.args[1:]))

# リストの中身を絶対値にして1要素ずつ出力
for n in num:
    print(abs(n), end="") 