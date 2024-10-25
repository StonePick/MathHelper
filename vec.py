"""Vectors calculator. Legacy version. Supports 2D and 3D only."""

import math

#Define 2D vectors
def vec_def_2d(dx:float=0,dy:float=0) -> tuple:
    return dx,dy,0

#Define 3D vectors
def vec_def_3d(dx:float=0,dy:float=0,dz:float=0) -> tuple:
    return dx,dy,dz

#Vectors addition calculation
def vec_cal_add(*vec:tuple,reverse:bool=0) -> tuple:
    if (reverse == 0): #judge if subtraction mode is on, 0 is OFF
        sx = 0
        sy = 0
        sz = 0
        #x
        for i in vec:
            sx += i[0]
        #y
        for i in vec:
            sy += i[1]
        #z
        for i in vec:
            sz += i[2]
    if (reverse == 1): #subtraction mode
        sx = 2 * vec[0][0]
        sy = 2 * vec[0][1]
        sz = 2 * vec[0][2]
        #x
        for i in vec:
            sx -= i[0]
        #y
        for i in vec:
            sy -= i[1]
        #z
        for i in vec:
            sz -= i[2]
    return sx,sy,sz

#Vectors scalar multiplication calculation
def vec_cal_mul(vec1:tuple,vec2:tuple) -> float:
    mul = vec1[0]*vec2[0]+vec1[1]*vec2[1]+vec1[2]*vec2[2]
    return mul

#Vectors dot product calculation
def vec_cal_dot(cof:float,vec:tuple) -> tuple:
    dot = (cof*vec[0],cof*vec[1],cof*vec[2])
    return dot

#Vectors module calculation
def vec_cal_mod(vec:tuple) -> float:
    sqrmod = vec[0] ** 2 + vec[1] ** 2 + vec[2] ** 2
    mod = sqrmod ** (1/2)
    return mod

#Vectors cross product calculation
def vec_cal_crs(vec1:tuple,vec2:tuple) -> tuple:
    #vec1
    l = vec1[0]
    m = vec1[1]
    n = vec1[2]
    #vec2
    o = vec2[0]
    p = vec2[1]
    q = vec2[2]
    #calculation
    crs = (m*q - n*p,n*o - l*q,l*p - m*o)
    return crs

#Vectors angle calculation
def vec_cal_ang(vec1:tuple,vec2:tuple,sinmode:bool=0) -> float:
    mul = vec_cal_mul(vec1,vec2)
    modmul1 = vec_cal_mod(vec1)
    modmul2 = vec_cal_mod(vec2)
    angcos = mul / (modmul1 * modmul2)
    if (sinmode == 0):
        return angcos
    else:
        angsin = (1-angcos**2)**(1/2)
        return angsin

#Vectors vertical judgement
def vec_jud_ver(vec1:tuple,vec2:tuple) -> bool:
    mul = vec_cal_mul(vec1,vec2)
    if (mul == 0):
        return True
    else:
        return False

#Vectors parallel judgement
def vec_jud_par(vec1:tuple,vec2:tuple) -> bool:
    a = vec1[0] / vec2[0]
    b = vec1[1] / vec2[1]
    c = vec1[2] / vec2[2]
    if a == b == c:
        return True
