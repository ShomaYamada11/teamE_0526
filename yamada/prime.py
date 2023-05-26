import sys
args = sys.argv
#引数を変数に代入
Num = int(args[1])
#関数を定義
def prime(num):
  '''引数までの素数をリストに格納'''
  primes = []
  for i in range(2, num):
    primes.append(i)
    for p in range(2, i):
      if i % p == 0:
        primes.remove(i)
        break
  return primes

#引数が1000以上か判定
if Num >= 1000:
  print("1000以上は判定できません", end="")

else:
    #リストの素数で割ってみて一度も割れなければ素数
    primes_list = prime(Num)
    for j in range(len(primes_list)):
        if Num % primes_list[j] == 0:
            print("not", end="")
            break
        elif j == len(primes_list) - 1:
            print("Prime", end="")
