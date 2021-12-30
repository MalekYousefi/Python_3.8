str_tmp="codecup6"
str_lenght=len(str_tmp)
str_list=[]
n=int(input())
for i in range(1, n+1):
    if(i-str_lenght>0):
        str_list.append(str_list[i-str_lenght-1])
    else:
        str_list.append(str_tmp[i-1])
print(str_list[i-1])