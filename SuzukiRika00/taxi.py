import sys
args = sys.argv

m = int(args[1])
price = 630

if m > 1500:
    distance = m - 1500
    adding_fee = ((distance // 344) + 1) * 98 
    price = price + adding_fee

print(price, end="")
