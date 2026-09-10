import numpy as np

# ----- indexing operations -----

a = np.arange(12)      # a: [ 0  1  2  3  4  5  6  7  8  9 10 11]
print(a[0])             # 0
print(a[-1])            # 11
print(a[2:5])           # [2 3 4]
print(a[:3])            # [0 1 2]
print(a[3:])            # [ 3  4  5  6  7  8  9 10 11]
print(a[::2])           # [ 0  2  4  6  8 10]
print(a[::-1])          # [11 10  9  8  7  6  5  4  3  2  1  0]

a2 = a.reshape(3, 4)    # a2: [[ 0  1  2  3]
                        #      [ 4  5  6  7]
                        #      [ 8  9 10 11]]
print(a2[1])             # [4 5 6 7]
print(a2[1, 2])          # 6
print(a2[1][2])          # 6, same result but creates an intermediate array
print(a2[:, 1])          # [1 5 9]
print(a2[0:2, 1:3])      # [[1 2]
                         #  [5 6]]
print(a2[..., 0])        # [0 4 8], ellipsis fills in remaining dimensions
print(a2[1, ...])        # [4 5 6 7]

b = a2[np.newaxis, :, :]  # adds a new axis
print(b.shape)             # (1, 3, 4)

mask = a2 % 2 == 0         # mask: [[ True False  True False]
                           #        [ True False  True False]
                           #        [ True False  True False]]
print(a2[mask])             # [ 0  2  4  6  8 10], boolean indexing flattens result
print(a2[a2 > 5])           # [ 6  7  8  9 10 11]

idx = np.array([0, 2])
print(a2[idx])              # [[ 0  1  2  3]
                            #  [ 8  9 10 11]], fancy indexing selects rows
print(a2[idx, idx])          # [ 0 10], pairs (0,0) and (2,2)
print(a2[[0, 1], [2, 3]])    # [2 7], pairs (0,2) and (1,3)

c = a2.copy()      # copying avoids modifying a2 through c
c[0, 0] = 99        # c: [[99  1  2  3]
                    #     [ 4  5  6  7]
                    #     [ 8  9 10 11]]
print(a2)            # [[ 0  1  2  3]
                     #  [ 4  5  6  7]
                     #  [ 8  9 10 11]], a2 unchanged

# ----- ndarray methods -----

m = np.array([[3, 1, 2], [6, 5, 4]])

print(m.shape)         # (2, 3)
print(m.ndim)           # 2
print(m.size)            # 6
print(m.dtype)            # int64

print(m.T)          # [[3 6]
                    #  [1 5]
                    #  [2 4]], transpose view
print(m.transpose())  # same as m.T
print(m.swapaxes(0, 1))  # same as m.T for a 2D array
print(m.reshape(3, 2))    # [[3 1]
                          #  [2 6]
                          #  [5 4]]
print(m.flatten())          # [3 1 2 6 5 4], always returns a copy
print(m.ravel())              # [3 1 2 6 5 4], returns a view when possible
print(m.astype(float))          # [[3. 1. 2.]
                                #  [6. 5. 4.]]

print(m.sum())          # 21
print(m.sum(axis=0))     # [9 6 6], sum of each column
print(m.sum(axis=1))      # [ 6 15], sum of each row
print(m.mean())             # 3.5
print(m.min())                # 1
print(m.max())                 # 6
print(m.argmin())               # 1, index into the flattened array
print(m.argmax())                # 3
print(m.cumsum())                 # [ 3  4  6 12 17 21]
print(m.std())                     # 1.707825127659933
print(m.var())                       # 2.9166666666666665

n = m.copy()
n.sort()                # n: [[1 2 3]
                        #     [4 5 6]], sorts each row in place
print(m.argsort())       # [[1 2 0]
                         #  [2 1 0]], indices that would sort each row
print(m.clip(2, 5))       # [[3 2 2]
                          #  [5 5 4]], values outside [2, 5] are clamped
print(m.round())            # [[3 1 2]
                            #  [6 5 4]], already integer valued
print(m.all())                # True, no zero elements
print(m.any())                 # True, at least one nonzero element
print(m.nonzero())               # (array([0, 0, 0, 1, 1, 1]), array([0, 1, 2, 0, 1, 2]))
print(m.tolist())                  # [[3, 1, 2], [6, 5, 4]]
print(m.item(0))                    # 3, first element as a Python scalar

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
print(v1.dot(v2))    # 32

v1.fill(7)            # v1: [7 7 7], sets all elements in place

sq = np.array([[1, 2], [3, 4]])
print(sq.trace())      # 5, sum of the diagonal
print(sq.diagonal())    # [1 4]

