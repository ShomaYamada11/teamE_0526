import sys

args = sys.argv

# 引数の格納
karaage = int(args[1])
calay = int(args[2])

# 売上の出力
print(760 * karaage +  850 * calay, end="")