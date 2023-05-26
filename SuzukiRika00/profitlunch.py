import sys
args = sys.argv

menu1 = int(args[1]) # 唐揚げ定食（760円/原価率32.3%）
menu2 = int(args[2]) # カレーセット（850円/原価率28.4%）

sales1 = 760 * menu1 # 各売上
sales2 = 850 * menu2 # 各売上
sales_sum = sales1 + sales2 # 売上合計

cost = round(sales1 * 0.323 + sales2 * 0.284) # 原価
profit = round(sales_sum - cost) # 粗利

print("売上高：{0}、原価：{1}、粗利：{2}".format(sales_sum, cost, profit), end="")