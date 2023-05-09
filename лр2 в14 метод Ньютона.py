import math
#f:= e^x - 2*(x-1)^2
a=0
b=1
#[a;b] = [0;1]
fa=math.exp(a)-2*(a-1)*(a-1)
fb=math.exp(b)-2*(b-1)*(b-1)
#f'(x) = e^x - 4x + 4
f1a= math.exp(a)-4*a+4
f1b= math.exp(b)-4*b+4
print("f'(a) =",fa)
print("f'(b) =",fb)
#f''(x) = e^x - 4
f2a= math.exp(a)-4
f2b= math.exp(b)-4
t = -1/5
n=1
x_n = 0
x_nn = x_n + t*(math.exp(x_n)-2*(x_n-1)*(x_n-1))
while abs(x_nn-x_n)>10**-8:
    t = -1/(math.exp(x_n)-4*x_n+4)
    x_n = x_nn
    x_nn = x_n + t*(math.exp(x_n)-2*(x_n-1)*(x_n-1))
    n+=1
print(x_nn, n)