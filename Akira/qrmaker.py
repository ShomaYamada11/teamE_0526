import sys 
import qrcode

args = sys.argv
URL_text = args[1]
# URL_text = str(URL_text)
count = 10


# ファイルを開く
with open(URL_text) as f:
    # 1行ずつ読み込む
    for line in f:
        #QRコードを生成する
        img = qrcode.make(line)
        #画像を保存
        img.save(f'../../output/{count}.png') #保存先のパス
        count += 1    #名前に使う数字のインクリメント









