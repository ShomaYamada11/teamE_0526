
import sys
args = sys.argv
import qrcode
import os

def make_qr(seq, url):      # QRコードを作成し保存する関数を定義
    path = os.path.join("..", "..", "Python", "output", str(seq) + ".png")      # 保存先のファイル名を生成
    img = qrcode.make(url)      # QRコードを作成
    img.save(path)      # QRコードを保存

with open(args[1], mode="r", encoding="utf-8") as f:    # urlのリストがあるファイルを読み込みモードで開く
    for i, line in enumerate(f):    # 1行ずつ読み込む
        make_qr(i, line)    # QRコードを作成する関数を呼び出す