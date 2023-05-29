# 引数を読み込めるようにする
import sys
from transinsert import Transport
from database import session
agev = sys.argv

# 引数の読み方
name = agev[1]

# 保存先のパス設定とopen
filename = "/home/matcha-23training/files/" + str(name)
trans_file = open(filename, mode="w", encoding="utf-8")

# dbの出力

# すべてのデータ取得
table_list = session.query(Transport).all()
# テーブルを１行ずつ書き込み
for list in table_list:
    trans_file.write('"' + str(list.date) + '"."' +'"' + str(list.seq) + '"."' +'"' + str(list.departure) + '"."' +'"' + str(list.arrival) + '"."' +'"' + str(list.via) + '"."' +'"' + str(list.amount) + '"\n')

# ファイル閉じる
trans_file.close()