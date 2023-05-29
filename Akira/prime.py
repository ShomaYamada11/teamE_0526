import sys

# 引数の取得
args = sys.argv
number = int(args[1])

# 1000以上かの判定
if number >= 1000:
    print("1000以上は判定できません", end="")

else: # 素数の判定
    for i in range(number):
        # １と０と自分以外で割り切れたら
        if number % (i+1) == 0 and 0 != i and number != (i+1):        
            print("not", end="")
            break

        # for回り終わったら
        elif number == i + 1: 
            print("prime", end="")


# for i in range(number):
#      if number % i and 1!= i and number != i :
#         if number % 2 == 1:
#             print("Prime")
#         else : print("not")

#         break
    
#     print("Prime")

          
          

