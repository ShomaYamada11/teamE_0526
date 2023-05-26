name_list = ["Kurita", "Tanaka", "Kaneda", "Noda", "Koyama", \
             "Adachi", "Kuriyama", "Ohyama", "Kishida"]             #リストを作成

odd_list = []       #奇数の添え字のみを入れるリストを作成

for i in range(len(name_list)):     #添え字の奇遇判定をするループ処理を作成
    if i % 2 == 1:
        odd_list.append(name_list[i])   #リストに追加する

print(odd_list, end="")