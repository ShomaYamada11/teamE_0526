import sys
args = sys.argv

num = int(args[1]) 


if num <= 1:
    print("prime", end="") # 1の場合「素数:prime」
elif num >= 1000:
    print("1000以上は判定できません", end="") # 1000以上の場合「不可」
else:
    for i in range(2, int(num**0.5)+1): # 素数かどうか判定
        if num % i == 0:
            print("not", end="")
            break
    else:
        print("prime", end="")

