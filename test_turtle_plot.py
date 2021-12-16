import turtle
import numpy as np
from matplotlib import pyplot as plt
n=20000
step=(5*3.14/n)*2
x=[]
y=[]
tmp_1=0
for i in range(1, n):
    tmp_1+=step
    x.append(tmp_1)
    tmp_2=turtle.math.sin(tmp_1)*100
    y.append(tmp_2)
a=np.array(x)
b=np.array(y)
plt.plot(a, b)
plt.show()