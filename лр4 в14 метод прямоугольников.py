import math
#f=((math.exp(x/(math.exp(1/2)))-math.exp(-x/(math.exp(1/2))))/2)**(1/3)
#f=(math.sinh(x/math.exp(1/2)))**(1/3)
a=2
b=6
n=24
delta=(b-a)/n
x0=a
int_f1=0
for i in range(n):
    x1=x0+delta
    zn=(x0+x1)/2
    f=((math.exp(zn/(math.exp(1/2)))-math.exp(-zn/(math.exp(1/2))))/2)**(1/3)
    #f=(math.sinh(zn/math.exp(1/2)))**(1/3)
    x0=x1
    int_f1+=f*delta
print(int_f1)