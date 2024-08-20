import numpy as np

a = np.array([[[1,2],[3,4]],[[1,2],[3,4]]])
print(a.ndim)

a = np.arange(10)
print(a)

a = np.zeros(5, int)
print(a)

a = np.concatenate(([[1,2,3]], [[6,7]]), axis=1)
print(a)