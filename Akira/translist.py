# 引数を読み込めるようにする
import sys
from transinsert import Transport
from database import session
agev = sys.argv

# 引数の読み方
name = agev[1]

filename = "/home/matcha-23training/files/" + str(name)
trans_file = open(filename, mode="w", encoding="utf-8")

# dbの出力
table_list = session.query(Transport).all()
for list in table_list:
    trans_file.write('"' + str(list.date) + '"."' +'"' + str(list.seq) + '"."' +'"' + str(list.departure) + '"."' +'"' + str(list.arrival) + '"."' +'"' + str(list.via) + '"."' +'"' + str(list.amount) + '"\n')


trans_file.close()