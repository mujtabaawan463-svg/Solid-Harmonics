from gbasis.spherical import real_solid_harmonic
from sympy import symbols, nsimplify, simplify
def real_spherical_harmonics(poly):
    x, y, z = symbols("x y z")
    expr = 0
    for (i, j, k), c in poly.items():
        expr += (nsimplify(c)) * (x**i)*(y**j)*(z**k)
    return(expr.simplify())
R21 = real_solid_harmonic(2, 2) 
print(R21)
expr = real_spherical_harmonics(R21)
print((expr))

