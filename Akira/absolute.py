import sys
args = sys.argv

# 引数をintに変換してリスのに格納
num =int(args[1])

# リストの中身を絶対値にして1要素ずつ出力
print(str(num)+" "+str(abs(num)),end="") 