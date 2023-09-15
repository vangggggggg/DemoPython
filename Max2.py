n = int(input())
a = [0]
a = list(map(int,input().split()))
a.sort()
b = max(a) 
for i in range(0,n):
    if a[n-i-1] != b:
        print(a[n-i-1])
        break
