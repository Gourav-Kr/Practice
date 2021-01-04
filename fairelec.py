t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    l1,l2=l1[:n],l2[:m]
    s=0
    if l1==l2:
        print(-1)
    else:
        l1.sort()
        l2.sort(reverse=True)
        l1s,l2s=sum(l1),sum(l2)
        for i in range(max(n,m)):
            if l1s>l2s:
                print(s)
                break
            else:
                try:
                    l1[i],l2[i]=l2[i],l1[i]
                    l1s,l2s=sum(l1),sum(l2)
                    s+=1
                except:
                    print(-1)
                    break 
