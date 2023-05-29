from database import session    
from tables import Transport   
import sys
args = sys.argv

listname = args[1] # 引数で名前入力
datalist = session.query(Transport).all() # 交通費精算テーブルの情報取得

list_file = open("listname", mode = "w", encoding="utf-8")  # ファイルを開く

for i in Transport.seq:
    list_file.write("datalist[i]")

list_file.close()