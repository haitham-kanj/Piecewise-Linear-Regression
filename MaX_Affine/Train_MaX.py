import numpy as np
import Max_Function

def Train_Max(parameters:dict, idx_s: int, idx_n: int) -> float:
    # Input Data:
    # parameters = {
    #   "d":    # Dimension of input vector (covariates)
    #   "s":    # Sparsity Level
    #   "sig":  # Noise standard deviation
    #   "M":    # Number of random initializations 
    #   "k":    # Number of linear models
    #   "n":    # Number of data points }
    # idx_s:    index of sparsity level from parameters["s"]
    # idx_n:    index of number of data points from parameters["n"]

    # Unwrap Data:
    n = parameters["n"][idx_n]
    s = parameters["s"][idx_s]
    d = parameters["d"]
    sig = parameters["sig"]
    M = parameters["M"]
    k = parameters["k"]

    # Generate Ground-Truth Model Parameters \in R^ (d+1) x k
    Model = np.zeros((d+1,k))
    Rand = np.random.normal(loc=0.0, scale=1.0, size=(d+1,k))
    for jj in range(k):
        Model[:,jj] =  Rand[:,jj]/np.linalg.norm(Rand[:,jj])

    # Generate Covariate Samples:
    X = np.vstack(np.random.normal(loc=0,scale=1,size=(d,n)),
                     np.ones(1,n)   )
    
    # Generate Measurements:
    y = Max_Function(X,Model,sig)

    # Initialization:
    Model_init = Initialize_MaX(k,y,X)
    # Sparse Gradient Descent (Sp-GD):

    # Estimation Error Calculation:
    err =0





    
    return err