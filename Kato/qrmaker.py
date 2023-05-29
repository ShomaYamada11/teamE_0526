
import sys
args = sys.argv
import qrcode
import os

def make_qr(seq, url):
    path = os.path.join("..", "..", "Python", "output", str(seq) + ".png") 
    img = qrcode.make(url)
    img.save(path)

with open(args[1], mode="r", encoding="utf-8") as f:
    for i, line in enumerate(f):
        print(line)
        make_qr(i, line)