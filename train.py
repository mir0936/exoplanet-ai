import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt

# Load data
data = np.loadtxt('lightcurves.csv', delimiter=',')
y = torch.tensor(data[:, 0], dtype=torch.float32).unsqueeze(1)
X = torch.tensor(data[:, 1:], dtype=torch.float32).unsqueeze(1) # Add channel dim for CNN

# Train/Test split
train_size = 8000
X_train, y_train = X[:train_size], y[:train_size]
X_test, y_test = X[train_size:], y[train_size:]

# Define 1D CNN
class TransitCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Sequential(
            nn.Conv1d(1, 16, kernel_size=5, padding=2),
            nn.ReLU(),
            nn.MaxPool1d(2),
            nn.Conv1d(16, 32, kernel_size=5, padding=2),
            nn.ReLU(),
            nn.MaxPool1d(2)
        )
        self.fc = nn.Sequential(
            nn.Linear(32 * 25, 64),
            nn.ReLU(),
            nn.Linear(64, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        x = self.conv(x)
        x = x.view(x.size(0), -1)
        return self.fc(x)

model = TransitCNN()
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Train
epochs = 10
losses = []
print("Training model...")
for epoch in range(epochs):
    optimizer.zero_grad()
    outputs = model(X_train)
    loss = criterion(outputs, y_train)
    loss.backward()
    optimizer.step()
    losses.append(loss.item())
    print(f"Epoch {epoch+1}/{epochs}, Loss: {loss.item():.4f}")

# Plot results
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
ax1.plot(losses, color='red')
ax1.set_title('Training Loss')
ax1.set_xlabel('Epoch')

# Plot a sample transit from the dataset
sample_idx = np.where(data[:, 0] == 1)[0][0]
ax2.plot(data[sample_idx, 1:], color='blue')
ax2.set_title('Sample Exoplanet Transit')
ax2.set_xlabel('Time Steps')
ax2.set_ylabel('Relative Flux')

plt.tight_layout()
plt.savefig('results.png')
print("Training complete. Plot saved as results.png.")
