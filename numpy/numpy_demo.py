import numpy as np
import os


def init():
    a = np.arange(30).reshape(3, 5, 2)
    print(f"a={a}")
    print(f"a.ndim:={a.ndim}")
    print(f"a.shape:={a.shape}")
    print(f"a.dtype:={a.dtype}")
    print(f"a.itemsize:={a.itemsize}")
    print(f"a.size:={a.size}")
    print(f"a.strides:={a.strides}")
    print(f"a.data:={a.data}")
    print(f"a.nbytes:={a.nbytes}")

def init1():
    a = np.zeros((3, 5), dtype=np.int32)
    print(f"a={a}")
    print(f"a.dtype:={a.dtype}")
    b = np.array([1, 2, 3, 4, 5],dtype=np.float64)
    print(f"b={b}")
    print(f"b.dtype:={b.dtype}")
    c = np.arange( 10, 30, 2 )
    print(f"c={c}")

def genFromTxt():
    a = np.genfromtxt('resources/numpy.txt', delimiter=',')
    print(f"a={a}")

#元素乘积
def multiply():
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([1, 2, 3, 4, 5])
    print(f"a*b={a*b}")

#矩阵乘积
def matrix():
    A = np.array( [[1,2],[0,3]] )
    B = np.array( [[2,0],[3,4]] )
    C = A @ B
    print(f"C={C}")

def random():
    a = np.random.random((3, 5))
    print(f"a={a}")

def test():
    a = np.arange(10)**3
    print(a)
    
genFromTxt()