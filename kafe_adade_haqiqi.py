temp_1, temp_2=input().split(" ")
n, k=float(temp_1), int(temp_2)
if(-2000000<=n<=2000000):
    if(0<=k<=50):
        for i in range(k):
            n/=2
        if(n>=0):
            print(int(n))
        elif(n<0):
            if((n-1)%(int(n)-1)==0): # (n<0 , n>-1)
                print(int(n))
            else:    
                print(int(n)-1)