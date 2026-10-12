from pylab import * 
xlim(0,10)
ylim(0,10)
def f(x): 
    y=x**2
    return y
pas=1
listex=[]
listey=[]
for i in range(0,20):
    x=-10+i*pas
    y=f(x)
    listex.append(x)
    listey.append(y)

plot(listex,listey,'--*')
show()
