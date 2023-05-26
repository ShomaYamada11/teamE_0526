import sys
args = sys.argv

#引数を変数に代入
frich_q = int(args[1])
curry_q = int(args[2])

#メニュー名と値段を辞書に追加
menus = {"唐揚げ定食":760, "カレーセット":850}

#売上高計算
sales = menus["唐揚げ定食"] * frich_q + menus["カレーセット"] * curry_q

#売上高出力
print(sales, end="")