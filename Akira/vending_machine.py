class Vending_Machine():
    def __init__(self) :
        self.product_list = {"お茶":110,
                        "コーヒー":100,
                        "ソーダ":160,
                        "コーンポタージュ":130,
                        }
        self.change_list = {"5000円札：":0,
                           "1000円札：":0,
                           "100円玉：":0,
                           "50円玉：":0,
                           "10円玉：":0
                        }

        print(self.product_list)
        self.money = 0

    def print_list(self):
        
        for list in self.product_list:
            if self.product_list[list] < self.money:
                print(f"{list}{self.product_list[list]}")
        




    def input_money(self, money):
        self.money = money
        Vending_Machine().check_input_money(self.money)


    def check_input_money(self, money):
        if money > 10000:
            print("10,000を超える金額は投入できません。再度金額を投入してください")
            return True
        elif money%10 != 0:
            print("1円玉5円玉は使用できません。再度金額を投入してください")
            return True
        elif money < min(self.product_list.values()):
            print(f"{money}円では購入できる商品はありません。再度金額を投入してください")
            return True
        else: 
            self.money = money
            return False

    def buy_product(self,product_name):
        if product_name == "cansel":
            return False
        
        else:
            for key in self.product_list.keys() :
                if key == product_name:
                    product_price = self.product_list[product_name]
                    self.money = self.money - product_price
                    if self.money > min(self.product_list.values()):
                        if Vending_Machine().change_money(self.money) == True
                            print(f"残高{self.money}")                     
                            if  "Y" == input(print("続けて購入しますか（Y/N）")):
                                return True
                            else: return False
        
    def change_money(self):
        
        five_thousand_yen_cnt = self.money // 5000
        self.money -= 5000 * five_thousand_yen_cnt
        self.change_list["5000円札："] = five_thousand_yen_cnt

        one_thousand_yen_cnt = self.money // 1000
        self.money -= one_thousand_yen_cnt * 1000 
        self.change_list["1000円札："] =one_thousand_yen_cnt


        five_hundred_yen_cnt = self.money // 500
        self.money -= five_hundred_yen_cnt * 500
        self.change_list["500円玉："] =five_hundred_yen_cnt
 

        one_hundred_yen_cnt = self.money // 100
        self.money -= one_hundred_yen_cnt * 100 
        self.change_list["100円玉："] =one_hundred_yen_cnt


        five_ten_yen_cnt = self.money // 50
        self.money -= five_ten_yen_cnt * 50 
        self.change_list["10円玉："] =five_ten_yen_cnt


        one_ten_yen_cnt = self.money // 10
        self.money -= one_ten_yen_cnt * 10 
        self.change_list["5円玉："] =one_ten_yen_cnt

        print(self.change_list)
        for list in self.change_list:
            if self.change_list[list] != 0:
                print(f"{list}{self.change_list[list]}")

            






        


        

        

