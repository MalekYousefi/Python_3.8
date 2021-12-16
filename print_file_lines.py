f=open('data.txt','r') #data.txt must be in the current directory
for line in f.readlines():
    print(line,end='')
f.close