def sl (l,k): 
    base = []   
    lists = [base] 
    for i in range(len(l)): 
        orig = lists[:] 
        new = l[i] 
        for j in range(len(lists)): 
            lists[j] = lists[j] + [new] 
        lists = orig + lists                

    return lists


for i in range(int(input())):
    n,k=map(int,input().split())
    h=list(map(int,input().split()))
    h.sort(reverse=True)
    r=[]
    if sum(h)<2*k:
        print(-1)
    elif sum(h)==2*k:
        print(len(h))
    else:
            r=[]
            sub,l=sl(h,k),[]
            for i in sub:
                if sum(i)>=k and sum(i)<k+20:
                    l.append(i)
            t=l[0]
            for i in l:
               if sum(i)<sum(t):
                   if len(i)<=len(t):
                       t=i
            r.extend(t)
            for i in r:
                h.remove(i)
            sub,l=sl(h,k),[]
            for i in sub:
                if sum(i)>=k and sum(i)<k+20:
                    l.append(i)
            t=l[0]
            for i in l:
               if sum(i)<sum(t):
                   if len(i)<=len(t):
                       t=i
            r.extend(t)
            print(len(r))
        


