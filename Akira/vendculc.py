import sys
from vending_machine import Vending_Machine

vm = Vending_Machine()


money = int(input("投入金額を入力してください"))
while vm.input_money(money):
    money = int(input("投入金額を入力してください"))

product_name = input("何を購入しますか（商品名/cancel）")
while vm.buy_product(product_name):
    vm.print_list()
    product_name = input("何を購入しますか（商品名/cancel）")

vm.change_money()



