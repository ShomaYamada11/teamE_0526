# モジュールをインポート
import sys

# 引数を変数へ代入
args = sys.argv
num = int(args[1])


# 素数か判断
if num < 1: # 1以下でないか判断
    print("not", end="")

elif num >= 1000:
    print("1000以上は判定できません", end="")

else: # 引数の半分プラス1の要素数まで割り算し、余りが0になるかlimitまできたら終了
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            print("not", end="")
            break
    else: # 素数と判断
        print("prime", end="")