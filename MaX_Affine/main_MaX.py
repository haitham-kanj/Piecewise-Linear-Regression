# Imports:
import numpy as np
import matplotlib as mplot

# Variable Setup:
parameters = {
    "d":    200,                        # Dimension of input vector (covariates)
    "s":    np.arange(15,100+1,5),      # Sparsity Level
    "sig":  0.1,                        # Noise standard deviation
    "M":    100,                        # Number of random initializations 
    "k":    3,                          # Number of linear models
    "n":    np.arange(0.4e3,2e3+1,1e2), # Number of data points
}
parameters["size_s"] = parameters["s"].size
parameters["size_n"] = parameters["n"].size

# Simulate Sparse Max-Affine n Vs s graph:
Err = np.zeros((parameters["size_s"],parameters["size_n"]))
for ii in range(parameters["size_s"]):
    for jj in range(parameters["size_n"]):
        Err[ii,jj] =0
