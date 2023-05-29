def goods_display():
    '''商品と金額の一覧を表示'''
    for name in goods.keys():
        price = goods[name]
        goods_price_list.append(price)
        s = "{0}：{1}円".format(name, price)
        print(s)

def change(money):
    '''おつりの計算'''
    print("おつり")
    money_type = [5000, 2000, 1000, 500, 100, 50, 10]
    money_num = [0, 0, 0, 0, 0, 0, 0]

    '''各紙幣、小銭の必要枚数を計算'''
    for i in range(7):
        money_num[i] = money // money_type[i]
        money = money - money_type[i] * money_num[i]

    '''おつりを出力'''
    for i in range(7):
        if money_num[i] != 0:
            if i < 3:
                print(str(money_type[i]) + "円札：" + str(money_num[i]) + "枚")
            else:
                print(str(money_type[i]) + "円玉：" + str(money_num[i]) + "枚")

def question(money):
    '''購入商品orキャンセルの確認'''
    answer = input("何を購入しますか（商品名/cancel）")
    if answer == "cancel":
        change(money)
        return answer
    else:
        return answer

#投入金額の判定
def money_check(money,money_num):
    '''1円玉、5円玉がないかチェック'''
    if money_num[-1] != '0':
        remoney = input("1円玉、5円玉は使用できません。再度投入金額を入力してください")
        remoney_num = list(str(remoney))
        money_check(int(remoney),remoney_num)

    else:
        '''最低金額より小さくないかチェック'''
        if money >= min(goods_price_list):
            '''1万円を超えないかチェック'''
            if money > 10000:
                remoney = input("10000円を超える金額は投入できません。再度投入金額を入力してください")
                remoney_num = list(str(remoney))
                money_check(int(remoney),remoney_num)

            else:
                good = question(money)
                if good != "cancel":
                    money = money - goods[good]
                    money_check2(money)
            
        else:
            s2 = "{0}円では購入できる商品がありません。再度投入金額を入力してください".format(money)
            remoney = input(s2)
            remoney_num = list(str(remoney))
            money_check(int(remoney),remoney_num)

#残金が最低金額より低いか判定
def money_check2(money):
    if money < min(goods_price_list):
        change(money)
    else:
        print("残金：" + str(money) + "円")
        Y_or_N = input("続けて購入しますか（Y/N）")

        if Y_or_N == "Y":
            goods_display()
            nextgood = question(money)
            if nextgood != "cancel":
                money = money - goods[nextgood]
                money_check2(money)
        elif Y_or_N == "N":
            change(money)



#金額リストを作成
goods_price_list = []
goods = {"お茶":110, "コーヒー":100, "ソーダ":160, "コーンポタージュ":130}

#商品リストを表示
goods_display()

#金額投入
money = int(input("投入金額を入力してください"))
money_num = list(str(money))

#金額処理
money_check(money,money_num)