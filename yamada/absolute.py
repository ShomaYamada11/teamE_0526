import sys
args = sys.argv
#引数を変数に代入
num = int(args[1])
#絶対値を求める
abs_num = abs(num)
#出力
print(str(num) + " " + str(abs_num), end="")