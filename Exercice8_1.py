from pylab import * 
xlim(-3,3)
ylim(-20,20)
listex=[]
listey=[]
for i in range(100):
    x=-3+0.06*i
    y=x**3
    listex.append(x)
    listey.append(y)

plot(listex,listey,'--*')
show()