import numpy as np
import matplotlib.pyplot as plt

a = [[1,2,1],[2,3,2]]
b = [1,2]
a = np.delete(a,2,axis=1)
print(a)
diff = np.tile(b,(2,1))-a
print(diff)

c = [[1,2],[2,4]]  # X坐标
d = [[4,3],[3,5]]  # Y坐标
plt.plot(d,c,color='r')
plt.show()
