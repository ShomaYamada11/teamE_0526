import sys
args = sys.argv

number = int(args[1])   #引数をintに変換

if number >= 1000:      #1000以上が入力されたとき
    print("1000以上は判定できません", end="")

else:
    for i in range(2, number):    #素因判定のループ処理
        if number % i == 0:     #素数ではないとき   
            number /= i
            break

    if number == int(args[1]):
        print("Prime", end="")
    else:
        print("not", end="")
