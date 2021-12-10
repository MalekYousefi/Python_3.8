temp_1=int(input())
temp_2=int(input())
number_1=temp_1
number_2=temp_2
reverse_1=0
reverse_2=0
if 99<temp_1<1000:
    if 99<temp_2<1000:
        while(temp_1>0):
            reverse_1=(reverse_1*10)+(temp_1%10)
            temp_1//=10
        while(temp_2>0):
            reverse_2=(reverse_2*10)+(temp_2%10)
            temp_2//=10
        if reverse_1>reverse_2:
            print(number_2," < ",number_1)
        elif reverse_1<reverse_2:
            print(number_1," < ",number_2)
        else:
            print(number_1," = ",number_2)