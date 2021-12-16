n=int(input())
m=float(input())
BMI=n/(m*m)
print("%.2f"%BMI)
#print(int((BMI+0.0001)*100)/100)
if(1<=n<=200 and 1<=m<=10):
    if(BMI<18.5):
        print("Underweight")
    elif(18.5<=BMI<25):
        print("Normal")
    elif(25<=BMI<30):
        print("Overweight")
    else:
        print("Obese")