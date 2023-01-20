import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np


class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.predictor = nn.Sequential(
            nn.Linear(4, 2),
            nn.ReLU(),
            nn.Linear(2, 1)
        )

    def forward(self, x):
        return self.predictor(x)


# model creation
model = Model()


# training
X = np.random.rand(10, 4)
Y = ((X[:, 0] + X[:, 1]) > 0.5).astype(np.float32)

X = torch.Tensor(X)
Y = torch.Tensor(Y)

criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters())

for epoch in range(3):
    # reset optimizer
    optimizer.zero_grad()

    # forward + backward + optimize
    outputs = model(X)
    loss = criterion(outputs, Y)
    loss.backward()
    optimizer.step()


# inference
with torch.no_grad():
    X = torch.Tensor(np.random.rand(10, 4))

    for x, y in zip(X, model(X)):
        print(x, y)
