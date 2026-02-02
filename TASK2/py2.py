a=int(input("balance:"))
b=int(input("withdrawal amount"))
if b%100!=0:
  print("invalid withdrawal")
else:
  if b>a:
    print("insufficient balance")
  else:
    if (a-b)>=500:
      print("withdrawal successful")
    else:
      print("failed")