

name_list = ["Kurita",
             "Tanaka",
             "Kaneda",
             "Noda",
             "Koyama",
             "Adachi",
             "Kuriyama",
             "Ohyama",
             "Kisida"]

odd_name_list = []

for i in  range(len(name_list)):
    if i%2 == 1:
        odd_name_list.append(name_list[i])

print(odd_name_list,end="")