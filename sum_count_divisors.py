n=int(input())
cu=temp=0
if 1<=n<=5000:
    for i in range(1, n+1):
        for j in range(1, i//2+1):
            if((i%j)==0):
                cu+=1
                temp+=j
        cu+=1
        temp+=i
    print(cu,temp)