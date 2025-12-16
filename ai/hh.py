import numpy as np
a = np.arange(5000000)
np.save('array_file', a)
p=np.load("array_file.npy")
print(a[552])