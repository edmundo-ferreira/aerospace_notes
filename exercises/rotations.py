from sympy import *
from sympy.abc import theta, alpha, beta, phi, psi


m,g,ax,ay,az= symbols('m,g,ax,ay,az')
L,D,T,W,Lt = symbols('L,D,T,W,Lt')
V,Rz,Ry = symbols('V,Rz,Ry')

#Wind Axis
Ry_alfa = Matrix([[cos(-alpha), 0, sin(-alpha)], [0, 1, 0],[-sin(-alpha), 0, cos(-alpha)]])

Rz_beta = Matrix([[cos(beta),  -sin(beta),  0], [sin(beta), cos(beta), 0], [0, 0, 1]])


#Body Axis
Rx_phi   = Matrix([[1, 0, 0], [0, cos(phi),  -sin(phi)], [0, sin(phi), cos(phi)]])
Ry_theta = Matrix([[cos(theta), 0, sin(theta)], [0, 1, 0],[-sin(theta), 0, cos(theta)]])
Rz_psi   = Matrix([[cos(psi),  -sin(psi),  0], [sin(psi), cos(psi), 0], [0, 0, 1]])



#Wind to Body conversion
Twb = Ry_alfa* Rz_beta
Tbw = transpose(Twb)

#Body to NED conversion
Tbe = Rx_phi * Ry_theta * Rz_psi
Teb = transpose(Tbe)


#NED to Wind conversion
Tew = Tbw * Teb
Twe = transpose(Tew)



#aircraft forces
We = Matrix([[0],[0],[m*g]])
Fi =m*Matrix([[ax],[ay],[az]])

Fa = Matrix([[T-D],[0],[-L-Lt]])

Fg = Tew*We

Ft = Fg + Fa

Fiw= Tew*Fi

Total = (Fiw-Ft)



print(simplify(Total.subs([(beta,0),(psi,0),(phi,0),(D,0),(T,0),(Lt,0),(ay,0),(ax,0)])))




#print(simplify(Tew.subs([(beta,0),(psi,0),(phi,0)])))
