from pylab import * 
xlim(0,25)
ylim(0,45)
for i in range(21):
    x=i
    y=2*x
    y2=x
    y3=0.5*x
    plot(x,y,'dr')
    plot(x,y2,'ob')
    plot(x,y3,'*r')
    
show()