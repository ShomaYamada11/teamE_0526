import sys
from database import session
from transinsert import Transport

args = sys.argv

#保存先のパス設定
filepath = "./output/{0}.txt".format(args[1])
#ファイルを開く
trans_file = open(filepath, mode="w", encoding="utf-8")

#print
trans_list = session.query(Transport).all()
for trans in trans_list:
    day = trans.date
    a = trans.seq
    b = trans.departure
    c = trans.arrival
    d = trans.via
    e = trans.amount
    trans_file.write('"{0}","{1}","{2}","{3}","{4}","{5}"\n'.format(day, a, b, c, d, e))

#ファイルを閉じる
trans_file.close()