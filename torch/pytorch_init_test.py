import torch

def print_version():
    print(f"torch.__version__={torch.__version__}")


def create_random_tensor():
    a = torch.rand(3, 5, dtype=torch.float32)
    print(f"a={a}")

def create_empty_tensor():
    a = torch.empty(3, 5)
    print(f"a={a}")

def create_zero_tensor():
    a = torch.zeros(3, 5)
    print(f"a={a}")

def create_tensor_with_value():
    torch.set_printoptions(precision=16)
    a = torch.tensor([[1.2, 2.0, 3, 4.11, 5.2134578766],[2.31,1,1,1,1]], dtype=torch.double)
    print(f"a={a}")
    print(f"size={a.size()}")

print_version()
#create_random_tensor()
#create_empty_tensor()
#create_zero_tensor()
create_tensor_with_value()
