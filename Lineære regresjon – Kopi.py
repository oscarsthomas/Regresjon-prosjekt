import matplotlib.pyplot as plt
import pandas as pd
csv = input('Hva er navnet på csv filen? Ta med .csv på slutten: ')

xy = pd.read_csv(csv)

kolonnenavn = list(xy)
navnx = kolonnenavn[0]
navny = kolonnenavn[1]

x_1 = xy.groupby(navnx)[navnx].apply(lambda x: list(x)).tolist()
y_1 = xy.groupby(navny)[navny].apply(lambda x: list(x)).tolist()

x = []
y = []

for i in range(0, x_1.__len__()):
    a = x_1[i]
    b = y_1[i]
    x.append(a[0])
    y.append(b[0])
 

def stigningToPunkt(x,y):
    a = []
    b = x.__len__()
    for j in range(0, b):
        for i in range(0, b):
            q = (y[j]-x[j])/(y[i]-x[i])
            a.append(q)
    return a

def gjennomsnitt(x):
    g = 0
    a = x.__len__()
    for i in range(0,a):
        g = g + x[i]
    g = g/(a-1)
    return g

def konstantledd(a, x, y):
    b = []
    for i in range(0,y.__len__()):
        q = y[i] - a*x[i]
        b.append(q)
    return b
        

a_1 = stigningToPunkt(x, y)
a = gjennomsnitt(a_1)
b_1 = konstantledd(a, x, y)
b = gjennomsnitt(b_1)


x_1 = []
y_1 = []
for i in range(x[0]-1,x.__len__()+1):
    y_1.append(a*i+b)
    x_1.append(i)
    
plt.plot(x_1, y_1)
   

plt.plot(x, y, 'ro')
plt.xlabel('x-akse')
plt.ylabel('y-akse')
plt.title('Lineær regresjon')
plt.grid(True)
plt.show()
