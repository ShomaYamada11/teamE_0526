import sys
args = sys.argv

order_chikin = int(args[1])     #唐揚げ定食の注文数
order_curry = int(args[2])      #カレーセットの注文数

sales_total = order_chikin * 760 + order_curry * 850    #売り上げを計算

print(sales_total, end="")