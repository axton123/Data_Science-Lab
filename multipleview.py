import matplotlib.pyplot as plt
import numpy as np
t=np.arange(0.0,20.0,1)
s=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
s2=[4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,29,21,22,23]
plt.subplot(2,1,1)
plt.plot(t,s)
plt.ylabel('value')
plt.title('First Chart')
plt.grid(True)

plt.subplot(2,1,2)
plt.plot(t,s2)
plt.xlabel('Item (s)')
plt.ylabel('value')
plt.title('\n Second Chart')
plt.grid(True)
plt.show()
