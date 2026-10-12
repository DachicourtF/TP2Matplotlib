from pylab import * 
xlim(0,20)
ylim(2,4)
y=3
for i in range(10):
    x=5+i
    plot(x,y,'ob')
show()