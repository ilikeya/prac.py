num=int(input("Number of items: "))
total=float(0)
for i in range(0,num,1):
    price=float(input("price of items: "))
    total=total+price
if total>100:
    total=total-total*0.1
    print(total)
else:
     print(total)