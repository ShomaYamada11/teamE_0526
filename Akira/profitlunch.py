import sys

args = sys.argv

# 引数の格納
karaage = int(args[1])
calay = int(args[2])

# 売上の計算
karaage_sales = 760 * karaage 
calay_sales= 850 * calay
cales_sum = karaage_sales + calay_sales

# 原価の計算
karaage_prime_cost = round(karaage_sales * 0.323)
calay_prime_cost = round(calay_sales * 0.284)
prime_cost_sum = karaage_prime_cost + calay_prime_cost

# 粗利の計算
karaage_gross_profit = karaage_sales - karaage_prime_cost
calay_gross_profit = calay_sales - calay_prime_cost
gross_profit_sum = karaage_gross_profit + calay_gross_profit

# 売上、原価、粗利の出力
print("売上高：" + str(cales_sum) + "、" + "原価：" + str(prime_cost_sum) + "、" + "粗利：" + str(gross_profit_sum), end="")

