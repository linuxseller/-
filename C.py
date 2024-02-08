n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(1,n):
    a[i]=a[i-1]+a[i]
    b[i]=max(a[i], b[i-1])+b[i]
print(b[n-1])
