import numpy as np
from functools import lru_cache
from functions1 import factorial

__all__ = ['sin']

def sin(x, n):

    sumi = sum(((-1)**i * x**(2*i + 1))/(factorial(2*i + 1)) for i in range(n+1))

    return sumi

    