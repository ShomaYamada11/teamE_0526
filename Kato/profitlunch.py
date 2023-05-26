import sys
args = sys.argv
from decimal import Decimal, ROUND_HALF_UP

list_chikin = [760, 0.323]      #唐揚げ定食の値段と原価率をリストで定義
list_curry = [850, 0.284]      #カレーセットの値段と原価率をリストで定義

list_chikin[1] = Decimal(str(list_chikin[0] * list_chikin[1]))\
    .quantize(Decimal('0'), rounding=ROUND_HALF_UP)                 #唐揚げ定食の原価率を原価にアップデート
list_curry[1] = Decimal(str(list_curry[0] * list_curry[1]))\
    .quantize(Decimal('0'), rounding=ROUND_HALF_UP)                 #カレーセットの原価率を原価にアップデート
list_chikin.append(list_chikin[0] - list_chikin[1])     #唐揚げ定食の粗利を追加
list_curry.append(list_curry[0] - list_curry[1])     #唐揚げ定食の粗利を追加

order_chikin = int(args[1])#唐揚げ定食の注文数
order_curry = int(args[2])      #カレーセットの注文数
print(list_chikin)
print(list_curry)     

day_total = []     #1日の売上高、原価、粗利を入力するためのリストを定義

for i in range(3):  #1日の売上高、原価、粗利を入力するループ処理
    day_total.append(list_chikin[i] * order_chikin + list_curry[i] * order_curry)

print("売上高：{0}、原価率：{1}、粗利：{2}"\
      .format(day_total[0], day_total[1], day_total[2]), end="")    #結果を表示