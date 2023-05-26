import sys
args = sys.argv

number = int(args[1])    #引数の数字を受け取る
print("{0} {1}".format(number, abs(number)), end="")    #整数と絶対値を表記