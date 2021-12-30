t=int(input())
for i in range(0, t):
    temp_1, temp_2, temp_3=input().split(" ")
    n, s, a=int(temp_1), int(temp_2), int(temp_3)
    if(2<=n<=100 and 1<=s<=100000 and 1<=a<=1000):
        tmp=(s+(n-1)*a)/n
        if(tmp==int(tmp) and s>a):
            print(int(tmp)-a)
        else:
            print(-1)