import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])
print(arr[2])
print(arr[-1])

print(arr[1:4])
print(arr[3:])

reshaped = arr.reshape(2,3)
print(reshaped)