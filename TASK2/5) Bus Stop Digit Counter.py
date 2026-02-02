n=int(input())
ce=0
co=0
while n >0 :
    d=n%10
    if d%2==0:
        ce=ce+1
    else:
        co=co+1
    n=n//10
print("Even digit count:",ce)
print("Odd digit count:",co)
        
