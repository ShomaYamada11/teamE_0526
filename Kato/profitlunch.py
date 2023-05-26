import sys
args = sys.argv
from decimal import Decimal, ROUND_HALF_UP

list_chikin = [760, 0.323]      #唐揚げ定食の値段と原価率をリストで定義
list_curry = [850, 0.284]      #カレーセットの値段と原価率をリストで定義

order_chikin = int(args[1])
order_curry = int(args[2])     #唐揚げ定食の注文数 

day_total = []      #1日の売上高、原価、粗利を格納するリストを定義

list_chikin[0] = list_chikin[0] * order_chikin
list_curry[0] = list_curry[0] * order_curry     
day_total.append(list_chikin[0] + list_curry[0])
day_total.append(list_chikin[0] * list_chikin[1] + list_curry[0] * list_curry[1])
day_total[1] = Decimal(str(day_total[1])).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
day_total.append(day_total[0] - day_total[1])

print("売上高：{0}、原価：{1}、粗利：{2}"\
      .format(day_total[0], day_total[1], day_total[2]), end="")    #結果を表示
