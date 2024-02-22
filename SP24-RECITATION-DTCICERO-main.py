"""
CMPS 2200  Recitation 3.
See recitation-03.md for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y

def quadratic_multiply(x, y):
    return _quadratic_multiply(x.binary_vec, y.binary_vec).decimal_val

def _quadratic_multiply(x, y):
    if len(x) == 1 and len(y) == 1:
        return BinaryNumber(int(x[0]) * int(y[0]))

    x, y = pad(x, y)
    n = len(x)
    half_n = n // 2
    a, b = split_number(x)
    c, d = split_number(y)
    ac = _quadratic_multiply(a.binary_vec, c.binary_vec)
    bd = _quadratic_multiply(b.binary_vec, d.binary_vec)
    
    ad_bc = _quadratic_multiply((a + b).binary_vec, (c + d).binary_vec) - ac - bd

    result = ac + bit_shift(ad_bc, half_n) + bit_shift(bd, 2 * half_n)

    return result
    
    
def test_quadratic_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    result = f(x, y)
    
    return (time.time() - start)*1000



    
    

