temp_1, temp_2, temp_3=input().split(" ")
n, x, y=int(temp_1), int(temp_2), int(temp_3)
cu=0
if(1<=n, x, y<=100000):
    while(cu<n//x+1):
        if(((n-cu*x)/y)==int((n-cu*x)/y)):
            print(cu, (n-cu*x)//y)
            break
        cu+=1
if((cu*x)+(((n-cu*x)//y)*y)!=n):
    print(-1)