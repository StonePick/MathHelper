#Define 2D vectors
def vec_def_2d(dx:float=0,dy:float=0) -> tuple:
    return dx,dy,0

#Define 3D vectors
def vec_def_3d(dx:float=0,dy:float=0,dz:float=0) -> tuple:
    return dx,dy,dz


#Vectors addition calculation
def vec_cal_add(*vec:tuple,reverse:bool=0) -> tuple:
    sx = 0
    sy = 0
    sz = 0
    if (reverse == 0):                                                                          #judge if subtraction mode is on, 0 is OFF
        #sum up x
        for i in vec:
            sx += i[0]
        #sum up y
        for i in vec:
            sy += i[1]
        #sum up z
        for i in vec:
            sz += i[2]
    if (reverse == 1):
        print("Subtraction mode is left undone.Operation interrupted.")
        """
        for i in vec:
            sx = 2 * i[0]
            sx -= i[0]
        for i in vec:
            sy = 2 * i[1]
            sy -= i[1]
        for i in vec:
            sz = 2 * i[2]
            sz -= i[2]
        """
    return sx,sy,sz

#Vectors multiplication calculation
def vec_cal_mul(vec1:tuple,vec2:tuple) -> float:
    mul = vec1[0]*vec2[0]+vec1[1]*vec2[1]+vec1[2]*vec2[2]
    return mul

#Vectors linear calculation
def vec_cal_lin(cof:float,vec:tuple) -> tuple:
    lin = (cof*vec[0],cof*vec[1],cof*vec[2])
    return lin

#Normal vector calculation
def vec_nor_cal():
    print("This function is left undone.Operation interrupted.")

#Normal vector Judgement
def vec_nor_jud(vec1:tuple,vec2:tuple,obj:tuple) -> bool:
    mul = vec_cal_mul(vec1,vec2)
    if (mul == 0):
        return True
    else:
        return False