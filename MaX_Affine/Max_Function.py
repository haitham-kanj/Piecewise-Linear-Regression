import numpy as np

def Max_Function(X,Model,sig)-> np.ndarray:
    # Input:
    # X:        Covariates \in R^ (d+1) x n
    # Model:    Model Parameters \in R^ (d+1) x k
    # sig:      Noise standard Deviation

    #Output:    Max-affine function evaluation
    yj = X.T @ Model
    y = yj.max(axis = 0) + np.random.normal(loc=0,scale=sig,size=(X.shape[1],1))
    return y