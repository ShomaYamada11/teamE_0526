import sys
args = sys.argv

num = int(args[1]) 


if num <= 1:
    print("prime", end="")
elif num >= 1000:
    print("1000以上は判定できません", end="")
else:
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            print("not", end="")
            break
    else:
        print("prime", end="")

