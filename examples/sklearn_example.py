from sklearn.svm import SVC
import numpy as np

X = np.random.rand(10, 2)
y = ((X[:, 0] + X[:, 1]) < 0.8).astype(np.int64)

# model creation & training
model = SVC().fit(X, y)

# inference
X = np.random.rand(10, 2)

for x, y in zip(X, model.predict(X)):
    print(x, y)
