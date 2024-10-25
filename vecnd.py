"""Vectors calculator with n-dimension support."""

import math

# Define n-dimensional vectors
def vec_def(*components: float) -> tuple:
    return components

# Vector addition/subtraction calculation
def vec_cal_add(*vec: tuple, reverse: bool = False) -> tuple:
    dim = len(vec[0])
    result = [0] * dim
    if reverse:
        for i in range(dim):
            result[i] = 2 * vec[0][i]
        for v in vec:
            for i in range(dim):
                result[i] -= v[i]
    else:
        for v in vec:
            for i in range(dim):
                result[i] += v[i]
    return tuple(result)

# Vector scalar multiplication calculation
def vec_cal_mul(vec1: tuple, vec2: tuple) -> float:
    return sum(v1 * v2 for v1, v2 in zip(vec1, vec2))

# Vector dot product calculation
def vec_cal_dot(cof: float, vec: tuple) -> tuple:
    return tuple(cof * v for v in vec)

# Vector modulus (magnitude) calculation
def vec_cal_mod(vec: tuple) -> float:
    return math.sqrt(sum(v ** 2 for v in vec))

# Vector angle calculation
def vec_cal_ang(vec1: tuple, vec2: tuple, sinmode: bool = False) -> float:
    dot_product = vec_cal_mul(vec1, vec2)
    mod1 = vec_cal_mod(vec1)
    mod2 = vec_cal_mod(vec2)
    angcos = dot_product / (mod1 * mod2)
    if sinmode:
        return math.sqrt(1 - angcos ** 2)
    return angcos

# Vector vertical (orthogonal) judgement
def vec_jud_ver(vec1: tuple, vec2: tuple) -> bool:
    return vec_cal_mul(vec1, vec2) == 0

# Vector parallel judgement
def vec_jud_par(vec1: tuple, vec2: tuple) -> bool:
    ratios = [v1 / v2 if v2 != 0 else float('inf') for v1, v2 in zip(vec1, vec2)]
    return all(r == ratios[0] for r in ratios)

# Vector cross product calculation (limited to 3-dimensional vectors)
def vec_cal_crs(vec1: tuple, vec2: tuple) -> tuple:
    if len(vec1) == 3 and len(vec2) == 3:
        l, m, n = vec1
        o, p, q = vec2
        return (m * q - n * p, n * o - l * q, l * p - m * o)
    raise ValueError("Cross product is only defined for 3-dimensional vectors.")
