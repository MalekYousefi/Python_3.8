n=int(input())
for i in range(0, n):
    for j in range(0, i+1):
        temp=1
        if(j>i-j):
            j=i-j
        for k in range(0, j):
            temp*=(i-k)
            temp//=(k+1)
        print(temp,"", end="")
    print()