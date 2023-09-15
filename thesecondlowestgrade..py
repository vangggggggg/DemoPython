n = int(input())
a =[0]*n
if 2<=n<=5:
    # f = input().split()
    # g = list(map(float,input().split()))
    for i in range(0,n):
        a[i] = [0]*2
        a[i][0] = input()
        a[i][1] = float(input())
        # a[i][0] = f[i]
        # a[i][1] = g[i]
    #sap xep theo tu phan tu minh muon trong mang
    c = min(a,key = lambda x:x[1])
    a.sort(key = lambda x:x[1])
    for i in range(n):
        if a[i][1] != c[1]:
            b = a[i][1]
            break;
    c = a
    c.sort()
    for i in range(n):
        if c[i][1] == b:
            print(a[i][0])
pass
