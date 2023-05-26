import sys
args = sys.argv

#メニュー名と値段を辞書に追加
menus = [760, 850]
cost_rate = [0.323, 0.284]

#売上高、原価、粗利のリスト作成
sales = []
prime_costs = []
profits = []

#それぞれの合計額の変数に0を代入
total_sales = 0
total_prime_costs = 0
total_profits = 0

#メニューごとにそれぞれ計算し、リストに追加
for i in range(len(menus)):
    #計算
    sale = menus[i] * int(args[i+1])
    prime_cost = round(sale * cost_rate[i])
    profit = sale - prime_cost
    
    #リストに追加
    sales.append(sale)
    prime_costs.append(prime_cost)
    profits.append(profit)

    #それぞれの合計額を計算
    total_sales = total_sales + sales[i]
    total_prime_costs = total_prime_costs + prime_costs[i]
    total_profits = total_profits + profits[i]

#出力
print("売上高：" + str(total_sales) + "、原価：" + str(total_prime_costs) + "、粗利：" + str(total_profits), end="")

