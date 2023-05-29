'''
from database import session    
from tables import Transport   
import sys
args = sys.argv

listname = args[1] # 引数で名前入力
datalist = session.query(Transport).all() # 交通費精算テーブルの情報取得

list_file = open("listname", mode = "w", encoding="utf-8")  # ファイルを開く

for i in Transport.seq:
    list_file.write(datalist[i])

list_file.close()
'''

from database import session    #１．データベースへの接続
from tables import Transport    #２．テーブル定義
import sys
args = sys.argv

# データを取得する
Translist=session.query(Transport).all()

#ファイルを開く
with open("C:\home\matcha-23training\TEAME_0526\SuzukiRika00" + args[1] , mode="w", encoding="utf-8") as f:
#DBから取得したデータを書き込み    
    for linedata in Translist:
        #日付はYYYYMMDDに加工して出力する。""囲みと,区切りで出力。最後は改行あり
        f.write("\"" + str(linedata.date.strftime("%Y%m%d")) \
                + "\",\"" + str(linedata.seq) + "\",\"" + linedata.departure + "\",\"" + linedata.arrival \
                + "\",\"" +linedata.via +"\",\"" + str(linedata.amount) +"\"\n")
        
        
        
