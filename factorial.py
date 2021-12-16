n=int(input())
fct=1
if 1<=n<=10:
    while(n>0):
        fct*=n
        n-=1
    print(fct)