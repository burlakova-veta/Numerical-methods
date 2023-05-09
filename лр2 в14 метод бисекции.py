import math
#f:= e^x - 2*(x-1)^2
a=0
b=1
#[a;b] = [0;1]
if fa*fb>0:
    while abs(b-a)>=10**-8:
        f1=math.exp(a)-2*(a-1)*(a-1)
        f2=math.exp(a+(b-a)/2)-2*(a+(b-a)/2-1)*(a+(b-a)/2-1)
        if f1*f2<0:
            b=a+(b-a)/2
        else:
            a=a+(b-a)/2
    x=a
print("x =",(x))