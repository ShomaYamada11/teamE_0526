
# リストの作成
name_list = ["Kurita",
             "Tanaka",
             "Kaneda",
             "Noda",
             "Koyama",
             "Adachi",
             "Kuriyama",
             "Ohyama",
             "Kisida"]

# 要素番号が奇数の要素を格納する配列
odd_name_list = []

# 要素番号が奇数の名前をodd_name_listに格納
for i in  range(len(name_list)):
    if i%2 == 1:
        odd_name_list.append(name_list[i])

# odd_name_listの表示
print(odd_name_list,end="")