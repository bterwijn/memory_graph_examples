import memory_graph as mg
import numpy as np

mg.extend_numpy()  # show ndarray as table
mg.config.type_to_slicer[np.ndarray] = (mg.Slicer(), mg.Slicer())  # show full matrices

print("\n=== Create data")
N = 20
D = 5
K = 3  # reduction from D to K dimensions
X = np.random.rand(N, D)
print(f'{X.shape=}')

print("\n=== Center X")
u = np.mean(X, axis=0)
XC = X - u  # X but shifted so it's centered
print(f'{XC.shape=}')

print("\n=== Compute covariance")
Covar = np.cov(XC.T, bias=True)
Covar2 = XC.T @ XC / XC.shape[0]  # alternative way to compute covariance
assert np.allclose(Covar, Covar2)  # check if they are (almost) equal
print(f'{Covar.shape=}')

print("\n=== Eigen Decomposition")
EigVal, EigVec = np.linalg.eig(Covar)
print(f'{EigVal.shape=}')
print(f'{EigVec.shape=}')

print("\n=== Check Eigvec Orthonormality, just to see things are alright, skip this normally")
lengths = np.linalg.norm(EigVec, axis=0)  # compute lengths of column vectors
assert np.allclose(lengths, np.ones(lengths.shape))  # lengths are close to 1
for c1 in range(EigVec.shape[1]):
    for c2 in range(c1+1, EigVec.shape[1]):
        d = np.dot(EigVec[:,c1], EigVec[:,c2])  # dot all combinations of column vectors
        assert np.fabs(d) < 0.0000001  # orthogonal to each other: dot product close to 0

print("\n=== Build projection matrix with K eigen vectors with highest eigen values")
W = EigVec[:, :K]
print(f'{W.shape=}')

print("\n=== Project from D to K dimension space")
Z = XC @ W
print(f'{Z.shape=}')

print("\n=== Reconstruct X from Z as good as possible")
XR = Z @ W.T + u
print(f'{XR.shape=}')
ReconstructError = X - XR
