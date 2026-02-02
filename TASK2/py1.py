n=input()
length=len(n)
half=length//2
sumf=0
sums=0
for i in range(half):
    sumf+=int(n[i])
for i in range(half,length):
    sums+=int(n[i])
if sumf==sums:
    print("balanced")
else:
    print("not balanced")