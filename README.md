# Convex-Piecewise-Linear-Regression
This repository presents the codes used to implement piecewise linear regression. 
Let y = f(x) + z be a univariate model with x having d variables. 
Only s out of d variables from x contribute to the model of y.
Learning peicewise linear models includes:
1. Parameter initialization: requires min(d,poly(s)) data samples.
   Summary: Sparse principal component analysis (sPCA), followed by search along the subspace defined by the principal components.
2. Parameter Retrieval up to arbitrarily small error: requires O(slog(d/s)) data samples.
   Summary: "Generalized" gradient descent with time varying block-wise step size followed by projection to feasibility set. Both steps are repeated until stop criterion is met.
