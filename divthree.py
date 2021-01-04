t=int(input())
for i in range(t):
    n,k,d=map(int,input().split())
    l=list(map(int,input().split()))
    s=sum(l)
    if s<k:
        print(0)
    else:
        if s<(k*d):
            print(s//k)
        else:
            print(d)
