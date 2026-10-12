from pylab import * 
xlim(-5,5)
ylim(-50,50)
listex=[]
listey=[]

for i in range(250):
    x=-5+0.02*i
    y=1/x
    listex.append(x)
    listey.append(y)
for i in range(250):
    x=0.02+0.02*i
    y=1/x
    listex.append(x)
    listey.append(y)

plot(listex,listey,'g')
show()