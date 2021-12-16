number_str=input()
number=int(number_str)
temp_1=abs(number)
temp_2=temp_3=0
number_counter=zero_counter=counter=0
number_length=len(number_str)
if(abs(number)<10**99): #If the length of number is less than 100 (Pos or Neg)
    if(number==0): #If the number is zero (without negative sign), number of zeros is the length of number
        zero_counter=number_length
        while(zero_counter>0):
                print(str(0)+":")
                zero_counter-=1
    else: #If the number is not zero (Pos or Neg)
        while(temp_1//10>0):
            temp_1//=10
            number_counter+=1
        number_counter+=1 #Number of digits after zero
        zero_counter=number_length-number_counter # Number of zeros before digits
        if(number<0): #If the number is negative
            zero_counter-=1 #Not counting negative sign before number
        if(zero_counter>0): #If we have zeros before digits
            while(zero_counter>0):
                print(str(0)+":")
                zero_counter-=1
        temp_1=abs(number)
        while(number_counter>0): #Get the first out of place number
            temp_1//=(10**(number_counter-1))
            if(temp_1==0):
                print(str(temp_1)+":")
            else:
                counter=temp_1
                temp_2=temp_1
                while(counter>1): #Print to number
                    temp_3=temp_2*10+temp_1
                    temp_2=temp_3
                    counter-=1
                print(str(temp_1)+":",temp_2)
            temp_2=abs(number)
            temp_2%=(10**(number_counter-1)) #Divide remaining calculation (continued outside of place)
            temp_3=temp_2
            counter=0
            while(temp_3//10>0): #Get the length of outside of place
                counter+=1
                temp_3//=10
            if(counter<number_counter-2): #If outside of place is zero
                print(str(0)+":")
                counter=0
                number_counter-=2
            else:
                number_counter-=1
            temp_1=temp_2