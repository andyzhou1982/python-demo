import numpy as np
import torch

a = torch.tensor([[10,20,30],[40,50,60]], dtype=torch.long)
b = torch.tensor([[1,2,3],[4,5,6]], dtype=torch.long)

def tensor_add():
    c = a + b
    print(f"c={c}")

def tensor_sub():
    c = a - b
    print(f"c={c}")

#改变维度
def change_tensor_dimension():
    c = a.view(6,1)
    print(f"c={c}")

#tensor转numpy
def to_numpy():
    c = a.numpy()
    print(f"c={c}")
    print(f"c.type:=",type(c))

def from_numpy():
    c = np.array([[1,2,3],[4,5,6]])
    d = torch.from_numpy(c)
    print(f"d={d}")
    print(f"d.type:=",type(d))    

tensor_add()
tensor_sub()
change_tensor_dimension()
to_numpy()
from_numpy()