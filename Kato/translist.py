import sys
args = sys.argv
from create_trasport import session
from create_trasport import Transport
import os

path = os.path.join("..", "..", "Python", "output", args[1])    # 出力するテキストファイルのパスを作成

tras_lists = session.query(Transport).all()     # データベースから情報を抽出

with open(path, mode="w", encoding="utf-8") as f:   # 出力先のファイルを開く
    for translist in tras_lists:
        f.write("\"{0}\",\"{1}\",\"{2}\",\"{3}\",\"{4}\",\"{5}\"\n"\
                .format(translist.date, translist.seq, translist.departure,\
                         translist.arrival, translist.via, translist.amount))

