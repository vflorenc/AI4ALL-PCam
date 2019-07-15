import numpy as np
from scipy import signal
    
x = np.array([[1, 1, 1, 0, 0],
              [0, 1, 1, 1, 0],
              [0, 0, 1, 1, 1],
              [0, 0, 1, 1, 0],
              [0, 1, 1, 0, 0]],
             dtype='float')

w_k = np.array([[-1,1],],
               dtype='float')

print(x.shape, w_k.shape)
f = signal.convolve2d(x, w_k, 'valid')

print(f)
