def prime(n):
    for i in range(2, n//2+1):
        if(n%i==0):
            return False
            break
    return True
#================================
n=int(input())
prime_numbers=[[2, 3, 5, 7]]
odd_numbers=[1, 3, 5, 7, 9]
if(1<=n<=8):
    for i in range(1, n):
        prime_numbers.append([])
        for j in prime_numbers[i - 1]:
            for k in odd_numbers:
                temp = j * 10 + k
                if(prime(temp)==True):
                    prime_numbers[i].append(temp)
    for i in prime_numbers[n-1]:
        print(i)