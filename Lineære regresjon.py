import matplotlib.pyplot as plt

x = []
y = []

i = 0
while i <= 10:
    x.append(i)
    y.append(i + 1)
    i = i + 1
    



def stigningToPunkt(x,y):
    a = []
    b = x.__len__()
    for j in range(0, b-1):
        for i in range(0, b-1):
            q = (y[j]-x[j])/(y[i]-x[i])
            a.append(q)
    return a

def gjennomsnitt(x):
    g = 0
    a = x.__len__()
    for i in range(0,a-1):
        g = g + x[i]
    g = g/(a-1)
    return g

def konstantledd(a, x, y):
    b = []
    for i in range(0,y.__len__()-1):
        q = y[i] - a*x[i]
        b.append(q)
    return b
        

a_1 = stigningToPunkt(x, y)
a = gjennomsnitt(a_1)
b_1 = konstantledd(a, x, y)
b = gjennomsnitt(b_1)


x_1 = []
y_1 = []
for i in range(0,11):
    y_1.append(a*i+b)
    x_1.append(i)
    
plt.plot(x_1, y_1)
   

plt.plot(x, y, 'ro')
plt.grid(True)
plt.show()