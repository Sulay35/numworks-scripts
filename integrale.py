"""
This program aim to approximate the value of a specific function using the rectangle method
Credits : @Sulaymane Dagnet 

"""

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

def aproxIntegrale(n,p):
    fn = lambda x: (x**n)*(exp(-x))
    I = 0
    
    x1 = np.arange(0, 1+1/p, 1/p)
    fig, ax = plt.subplots()
    
    plt.plot(x1, fn(x1), 'bo')
    ax.plot(x1, fn(x1), c="cyan")
    
    for k in range(p):
        x = k/p
        ax.add_patch(Rectangle((x, 0), 1/p, fn((k+1)/p),color="red", alpha=0.5))
        I = I + fn(x)*(1/p)
    
    ax.text(0.3,exp(-1)/2,"I ≃ "+str(round(I,3)), fontsize=20)
    
    plt.title("Approximation d'une intégrale : méthode des rectangles")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    plt.show()
    
    return I
