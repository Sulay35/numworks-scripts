"""
This program aim to approximate the value of a specific function using the rectangle method
Credits : @Sulaymane Dagnet 

"""

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

def aproxIntegrale(a,b,p):
    f = lambda x: x
    I = 0
    coef = (b-a)/p
    
    x1 = np.arange(a, b+coef, coef)
    fig, ax = plt.subplots()
    
    plt.plot(x1, f(x1), 'bo')
    ax.plot(x1, f(x1), c="cyan")
    
   
    
    for k in range(p):
        x = k*coef
        
        
        ax.add_patch(Rectangle((k*coef, 0), coef, f(k*coef),  color="red", alpha=0.5))
        
        I = I + f(x)*coef
    
    ax.text(b/2, f(b)/2,"I ≃ "+str(round(I,3)), fontsize=20)
    
    plt.title("Approximation d'une intégrale : méthode des rectangles")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    plt.show()
    
    return I

aproxIntegrale(0,25,100)
