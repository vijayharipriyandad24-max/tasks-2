a=int(input())
top=0
for i in range(1,a):
    n=int(input())
    d=n%10
    if d>top:
        top =d
        
print(top)
    