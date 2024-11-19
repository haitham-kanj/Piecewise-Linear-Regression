import numpy as np
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import tensorflow
x = np.array([[1,2,3,4]])
print(x)
