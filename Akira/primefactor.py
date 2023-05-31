import sys


args = sys.argv
# 引数をintに変換し、変数に代入
number = int(args[1])
# 素数の2を代入
i = 2
# 結果を出力するリストを初期化
result = []
# iが引数の半分以下の間ずっと繰り返し
while i <= number / 2:
    # 割り切れる場合
    if number % i == 0:
        # 引数の値をiで割る
        number /= i
        # 結果のリストに格納
        result.append(i)
        # iを1加算せずに次の繰り返しへ
        continue
    # iを1加算
    i += 1
# 余った数値を結果のリストに格納
result.append(int(number))
print(result, end="")