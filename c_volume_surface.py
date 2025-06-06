# c) Calculate volume under z = x^2 + y^2 over 0 ≤ x, y ≤ 1 using numerical integration
import numpy as np
from scipy import integrate

def surface_function(x, y):
    return x**2 + y**2

volume, error = integrate.dblquad(surface_function, 0, 1, lambda x: 0, lambda x: 1)
print("Volume under the surface z = x^2 + y^2 over [0,1] x [0,1]:", volume)
