#ax^3+bx+c+y=0
#dy^3+ey+f+x=0
a=3.6
b=5.4
c=1.2
d=3.7
e=4.6
f=0.8
y1=0
x1=0
xn=1
yn=1
f1=a*xn**3+b*xn+c+yn
f2=d*yn**3+e*yn+f+xn
print(x1,y1)
'''while f1>10**-8 and f2>10**-8:
    oA=(3*a*x1*x1+b)*(3*d*y1*y1+e)-1
    a11=(3*d*y1**2+e)/oA
    a12=-1/oA
    a21=-1/oA
    a22=(3*a*x1**2+e)/oA
    f1=a*x1**3+b*x1+c+y1
    f2=d*y1**3+e*y1+f+x1
    xn=x1-a11*f1-a12*f2
    yn=y1-a21*f1-a22*f2
    x1=xn
    y1=yn'''
for i in range(11):
    oA=(3*a*x1*x1+b)*(3*d*y1*y1+e)-1
    a11=(3*d*y1**2+e)/oA
    a12=-1/oA
    a21=-1/oA
    a22=(3*a*x1**2+e)/oA
    f1=a*x1**3+b*x1+c+y1
    f2=d*y1**3+e*y1+f+x1
    xn=x1-a11*f1-a12*f2
    yn=y1-a21*f1-a22*f2
    x1=xn
    y1=yn
print(xn,yn)
f1=a*xn**3+b*xn+c+yn
f2=d*yn**3+e*yn+f+xn
print(f1,f2)