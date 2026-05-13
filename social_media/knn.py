import random
import numpy as np
from collections import Counter
mg.extend_numpy()

def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

class KNN:

    def __init__(self, k=3):  # k=3 is default value
        self.k = k

    def fit(self, X, y):  # fit the training samples and training labels
        # store the training data and training labels in the class instance
        self.X_train = X
        self.y_train = y

    def predict(self, X):  # predict new sample
        # for each of the sample, we want to get
        # the distance between the sample and all the training samples
        # predicted_labels = [self._predict_(x) for x in self.X_train] # x is one sample. we want to do it for all the samples in X
        return [self._predict_(x) for x in X]

    def _predict_(self, x):
        # computer distances
        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]
        # print(distances)

        # then get k nearest samples, and get labels
        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        print(f'{x} {k_nearest_labels=}')
        
        # majority vote, most common class label among the neighbors
        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]

# setup training set and model
n = 10
m = 100
classes = 3
X = [ np.array([random.randrange(m), random.randrange(m)])
     for i in range(n) ]        # get data
y = [ x[0]%classes for x in X]  # generate a class for each data element
knn = KNN(5)
knn.fit(X, y)

# get new data to classify
new_X = [ np.array([random.randrange(m), random.randrange(m)])
     for i in range(5) ]
new_X_classification = knn.predict(new_X)
print(new_X_classification)
