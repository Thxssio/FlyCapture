import numpy as np
import matplotlib.pyplot as plt

arr = np.array(frame['buffer']).reshape((frame['rows'], frame['cols']))
plt.imshow(arr, cmap='gray')
plt.show()
