import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: 1 / (1 + e^(-z))
        # return np.round(your_answer, 5)
        arr = []
        for i in z:
            x= round(1/(1+np.exp(-i)),5)
            arr.append(float(x))

        return np.array(arr)


    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: max(0, z) element-wise
        arr = []
        for i in z:
            x= round(max(0,i),5)
            arr.append(float(x))

        return np.array(arr)
