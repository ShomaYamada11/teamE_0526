#自販機のお釣りを計算するmainファイル
import vendchange
import vendlist

vend_list = vendlist.vend_list  #自販機の商品と値段を格納した辞書を設定

for vendkey in vend_list.keys():    #商品内容を出力
    print(str(vendkey) + '：' + str(vend_list[vendkey]) + "円")

money = int(input("投入金額を入力してください: "))  #投入金額の入力

#購入の可否を判断
if money > 10000:   #¥10,000以上のとき
    money = int(input("10,000円を超える金額は投入できません。\
                      再度投入金額を入力してください: "))
        
elif money < min(vend_list):    #お金が足りないとき
    money = int(input("{}円では購入できる商品がありません。\
                      再度投入金額を入力してください: ".format(money)))

elif money[-1] != 0:    #お金が足りないとき
    money = int(input("1円玉、5円玉は使用できません。\
                      再度投入金額を入力してください: "))

product_name = input("購入したい商品を選んでください: ")    #購入商品の入力

if vend_list[product_name] == None:    #リストにない商品が選択されたとき
    print("商品がありません。再度購入したい商品を選んでください: ")

product_price = vend_list[product_name]     #購入商品の値段を参照


while (money >= min(vend_list)) or (money > product_price):    #お釣りを出すまでのループ処理
    money = money - product_price
    if money < min(vend_list):
        break
    
    