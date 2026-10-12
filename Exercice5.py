from pylab import * 
xlim(0,20)
ylim(0,30)
for j in range(10):
    y=10+j
    for i in range(10):
        x=5+i
        plot(x,y,'ob')
    
show()