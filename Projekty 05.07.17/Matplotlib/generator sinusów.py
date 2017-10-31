import numpy as np
import matplotlib.pyplot as plt



x=np.linspace(0,10,100)
y=np.sin(x)
z=np.cos(x)
PI=np.pi


suma = y+z


fig=plt.figure()

#SUMA
a=fig.add_subplot(2,2,1)
a2=fig.add_subplot(2,2,1)
a3=fig.add_subplot(2,2,1)

a.plot(x, y, color='red', ls='--')
a2.plot(x, z, color='green', ls='--')
a3.plot(x, suma, color='blue', linewidth=4.0)

a.set_xlim(0, 2*PI)
a2.set_xlim(0, 2*PI)
a3.set_xlim(0, 2*PI)

a.set(title='Suma',
       ylabel='Y',
       xlabel='X')




plt.grid()
plt.show()


