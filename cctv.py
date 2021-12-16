side_1= [int(i) for i in input().split(" ")]
side_2= [int(i) for i in input().split(" ")]
side_3= [int(i) for i in input().split(" ")]
side_4=[0,0]
if(0<=side_1[0],side_2[0],side_3[0],side_1[1],side_2[1],side_3[1]<=10**8):
    if(side_1[1]==side_2[1]):
        side_4[0]=(side_1[0]+side_2[0])-side_3[0]
        side_4[1]=side_3[1]
        print(side_4[0], side_4[1])
    elif(side_1[1]==side_3[1]):
        side_4[0]=(side_1[0]+side_3[0])-side_2[0]
        side_4[1]=side_2[1]
        print(side_4[0], side_4[1])
    elif(side_2[1]==side_3[1]):
        side_4[0]=(side_2[0]+side_3[0])-side_1[0]
        side_4[1]=side_1[1]
        print(side_4[0], side_4[1])
    else:
        pass