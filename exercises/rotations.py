from sympy import *
from sympy.abc import theta, alpha, beta, phi, psi


#Wind Axis
Ry_alfa = Matrix([[cos(alpha), 0, -sin(alpha)], [0, 1, 0],[sin(alpha), 0, cos(alpha)]])
Rz_beta = Matrix([[cos(beta),  -sin(beta),  0], [sin(alpha), cos(alpha), 0], [0, 0, 1]])


#Body Axis
Rx_phi   = Matrix([[1, 0, 0], [0, cos(phi),  sin(phi)], [0, -sin(phi), cos(phi)]])
Ry_theta = Matrix([[cos(theta), 0, -sin(theta)], [0, 1, 0],[sin(theta), 0, cos(theta)]])
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
W = Matrix([[0],[0],[m*g]])



print(Tew.subs((beta,psi),(0,0)))
