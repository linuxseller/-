a,b=input(),input()

n1 = int(a+b)
n2 = int(b+a)

if n1==int(n1**0.5)**2 or n2==int(n2**0.5)**2: print("Yes")
else: print("No")
