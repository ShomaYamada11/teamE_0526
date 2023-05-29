import os
import qrcode

txtfile_path = "./qrlink.txt"
with open(txtfile_path, encoding="utf-8") as tf:
    #1行ずつファイルを読む
    for i, line in enumerate(tf):
        i = i + 1
        #1行ずつqrcode作成
        img = qrcode.make(line)

        path = os.path.join(".", "output", "{0}.png".format(i))
        img.save(path)