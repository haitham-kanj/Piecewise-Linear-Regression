import numpy as np

def Intialize_MaX(k:int,y:np.ndarray,X =np.ndarray)-> np.ndarray:
    #Input:
    #y:     n x 1 Max-affine function evaluation
    #X:     (d+1) x n Covariates (Last row is 1's)
    #k:     Number of linear segments
    d = X.shape[0]-1
    n = X.shape[1]

    # Subspace Estimation:
    if k>= d:
        U = np.identity(d)
    else:
        U = PCA_method(y,X,k,d,n)

    # Model Initialization
    
    


    return Model_Init


def PCA_method(y,X,k,d,n):
    Xtop = X[:-1,:]
    tmp = np.sum(Xtop*y,axis=1)/n
    M = tmp @ tmp.T + (X@np.diag(y)@X.T - np.sum(y)*np.identity(d))/n
    V, eigvalues = np.linalg.eig(M)
    indk = np.argsort(eigvalues)
    U = V[:,indk]
    return U