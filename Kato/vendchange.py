#自販機のお釣り計算用ファイル
def calc_charge(money, product_price):
    if money < product_price:
        print("商品を購入することができません")
        