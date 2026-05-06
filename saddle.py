import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


x = np.linspace(-2, 2, 200)
y = np.linspace(-2, 2, 200)
X, Y = np.meshgrid(x, y)
Z = X**2 - Y**2
#print(X)


fig = plt.figure(figsize=(20, 10))
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X, Y, Z, rstride=10, cstride=10)


r = 0.3  # radius of the ball
u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(0, np.pi, 100)
U, V = np.meshgrid(u, v)
X_sphere = r * np.cos(U) * np.sin(V)
Y_sphere = r * np.sin(U) * np.sin(V)
Z_sphere = r * np.cos(V) + r + 0.08


ax.plot_surface(X_sphere, Y_sphere, Z_sphere, color='black')

# Labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Potential (Z)')


plt.show()
