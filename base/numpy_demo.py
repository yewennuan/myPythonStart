import numpy as np

a = np.arange(30).reshape(2, 3, 5)
print(a)

print(a.shape)
print(a.ndim)
print(a.dtype.name)
print(a.itemsize)
print(a.size)
print(type(a))
b = np.array([6, 7, 8])
print(b)
print(type(b))
print(np.array([(1.5, 2, 3), (4, 5, 6)]))
print(np.array([[1, 2], [3, 4]], dtype=complex))


