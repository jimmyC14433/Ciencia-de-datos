import matplotlib.pyplot as plt 
import numpy as np 

x = np.linspace(-10 , 10, 100)
y = np.sin(x) 
plt.plot(x, y, marker="1")
plt.xlabel("X numeros")
plt.ylabel("Y numeros")
plt.show()