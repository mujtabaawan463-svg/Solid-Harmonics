import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.special import sph_harm


theta = np.linspace(0, np.pi, 100)   
phi = np.linspace(0, 2*np.pi, 100)   
theta, phi = np.meshgrid(theta, phi)


x = np.sin(theta) * np.cos(phi)
y = np.sin(theta) * np.sin(phi)
z = np.cos(theta)


Y = {
    'Y_00':sph_harm(0, 0, phi, theta),
    'Y_1-1': y,
    'Y_10': z,
    'Y_11': x,
    'Y_2-2': x*y,
    'Y_2-1': z*y,
    'Y_20': 2*z**2 - x**2 - y**2,
    'Y_21': x*z,
    'Y_22': x**2 - y**2
}


def plot_harmonic_box(Y_val, title):
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(111, projection='3d')

  
    r = np.abs(Y_val)
    ax.plot_surface(r*x, r*y, r*z, facecolors=plt.cm.viridis((r-r.min())/(r.max()-r.min())),
                    rstride=1, cstride=1, linewidth=0, antialiased=True)

    ax.set_title(title)
    
   
    ax.set_box_aspect([1,1,1]) 
    ax.grid(True, color='k', linestyle='--', linewidth=0.8) 
    ax.set_xticks([-1, 0, 1])
    ax.set_yticks([-1, 0, 1])
    ax.set_zticks([-1, 0, 1])
    

    
    plt.show()


plot_harmonic_box(Y['Y_00'], '$Y_{11}$')