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
u_CX = np.mean(XC, axis=0)
assert np.allclose(u_CX, np.zeros(u_CX.shape)), "not centered at origin"

print("\n=== Compute covariance")
Covar = np.cov(XC.T, bias=True)
Covar2 = XC.T @ XC / XC.shape[0]  # alternative way to compute covariance
assert np.allclose(Covar, Covar2), "Covar and Covar2 should be equal"
print(f'{Covar.shape=}')
varX = np.sum(np.diag(Covar))
print(f'{varX=}')

print("\n=== Eigen Decomposition")
EigVal, EigVec = np.linalg.eig(Covar)
print(f'{EigVal.shape=}')
print(f'{EigVec.shape=}')

print("\n=== Check Eigvec Orthonormality, just to see things are alright, skip this normally")
lengths = np.linalg.norm(EigVec, axis=0)  # compute lengths of column vectors
assert np.allclose(lengths, np.ones(lengths.shape)), "lengths should be close to 1"
for c1 in range(EigVec.shape[1]):
    for c2 in range(c1+1, EigVec.shape[1]):
        d = np.dot(EigVec[:,c1], EigVec[:,c2])  # dot all combinations of column vectors
        assert np.isclose(d, 0), "should be orthogonal to each other, dot close to 0"

print("\n=== Build projection matrix with K eigen vectors with highest eigen values")
W = EigVec[:, :K]
print(f'{W.shape=}')
sumK_EigVal = np.sum(EigVal[:K,])  # resulting variance after projection
print(f'{sumK_EigVal=}')

print("\n=== Project from D to K dimension space")
Z = XC @ W
print(f'{Z.shape=}')
CovarZ = np.cov(Z.T, bias=True)
varZ = np.sum(np.diag(CovarZ))
print(f'{varZ=}')
assert np.allclose(sumK_EigVal, varZ), "variance should be sum of K EigVals"
assert varZ <= varX, "total variance in Z should be smaller (or equal) to that in X"

print("\n=== Reconstruct XR from Z as close as possible to X")
XR = Z @ W.T + u
print(f'{XR.shape=}')
ReconstructErrors = X - XR
CovarXR = np.cov(XR.T, bias=True)
varXR = np.sum(np.diag(CovarZ))
print(f'{varXR=}')
assert np.isclose(varZ, varXR), "total variance in XR should be same as in Z"
