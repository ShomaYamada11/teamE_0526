import sys
args = sys.argv

menu1 = int(args[1]) # 唐揚げ定食（760円）
menu2 = int(args[2]) # カレーセット（850円）

price = (760 * menu1) + (850 * menu2)
print(price, end="")