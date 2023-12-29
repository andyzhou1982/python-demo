import numpy as np


#soft_x1 = np.exp(x1)/(np.exp(x1)+np.exp(x2))
#自然对数的x1次方
def softmax(arr=[[-1.5607,  1.6123],[ 4.1692, -3.3464]]):
    soft1 = np.exp(arr[0][0])/ ( np.exp(arr[0][0]) + np.exp(arr[0][1]) )
    soft2 = np.exp(arr[0][1])/ ( np.exp(arr[0][0]) + np.exp(arr[0][1]) )
    soft3 = np.exp(arr[1][0])/ ( np.exp(arr[1][0]) + np.exp(arr[1][1]) )
    soft4 = np.exp(arr[1][1])/ ( np.exp(arr[1][0]) + np.exp(arr[1][1]) )
    print(f"soft1={soft1}")
    print(f"soft2={soft2}")
    print(f"soft3={soft3}")
    print(f"soft4={soft4}")

softmax()