def test(i,c):
    if len(i)==1:
        if i[0]=='0':
            print(c[0],end="")
        else:
            print(c[1],end="")
    else:
        d=i.pop(0)
        if d=='0':
            c=c[0:len(c)//2]
            return test(i,c)
        else:
            return test(i,c[len(c)//2:])
t=int(input())
ch=list(map(chr, range(97, 113)))
for i in range(t):
    l=[]
    n=int(input())
    s=input()
    for i in range(0,n,4):
        l.append(s[i:i+4])
    for i in l:
        i=list(i)
        test(i,ch)
    print()