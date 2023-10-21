import math
import torch

def test_grad():
    '''
    x = torch.ones(2, 2, requires_grad=True)
    print(f"x={x}")
    y = x + 2
    '''
    y=torch.tensor([[3.0,3.0],[3.0,3.0]],requires_grad=True)
    z = y * y * 3
    print(f"z={z}")
    out = z.mean() #将所有元素相加并除以元素的数量，得到平均值
    print(f"out={out}")
    out.backward()
    #print(f"x.grad={x.grad}")
    print(f"y.grad={y.grad}")

def f(x):
    return x**2

#计算导数
def derivative(f, x):
    h = 1e-6
    return (f(x + h/2) - f(x-h/2)) / h

def print_derivative():
    for x in range(10):
        derivative_at_x = derivative(f, x)
        print(derivative_at_x)

test_grad()
