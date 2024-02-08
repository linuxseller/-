n,b,g=int(input()),int(input()),int(input())
n*=2
while n>0 or (b>0 and g>0):
    if b>0:
        b-=2
        n-=1
    if g>0:
        g-=2
        n-=1
    if b>0:
        b-=3
        n-=1
    if g>0:
        g-=3
        n-=1
if n>=0 and b<=0 and g<=0:
    print("Yes")
else:
    print("No")
