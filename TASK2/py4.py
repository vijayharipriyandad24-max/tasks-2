a=int(input("Enter a age: "))
tprice =200
if a<5:
    print("ticket free:")
elif a>5 and 12<=a:
    fprice=tprice*0.5
    print("ticket price is:",fprice)
elif a>12 and 65<=a:
    print("full ticket price:",tprice)
elif a>=60 :
    fprice=tprice*0.3
    print("ticket price is:",fprice)
else:
    print("invalid age")