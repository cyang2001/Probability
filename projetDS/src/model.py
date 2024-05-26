import torch.nn as nn
import torch.nn.functional as F

class MyDataset(nn.utils.data.dataset):
    def __init__(self):
        super
class Model_DL(nn.Module):
    def __init__(self):
        super(Model_DL, self)
        self.fc1 = nn.Linear(in_features=10, out_features=30)
        self.bn1 = nn.BatchNorm1d(30)
        self.fc2 = nn.Linear(in_features= 30, out_features= 60)
        self.bn2 = nn.BatchNorm1d(60)
        self.fc3 = nn.Linear(in_features= 60, out_features= 30)
        self.bn3 = nn.BatchNorm1d(30)
        self.out = nn.Linear(in_features=30, out_features=1)
        self.active = F.relu()
    
    def forward(self, x):
        x = self.active(self.fc1(x))
        x = self.bn1(x)
        x = self.active(self.fc2(x))
        x = self.bn2(x)
        x = self.active(self.fc3(x))
        x = self.bn3(x)
        x = self.out(x)
        return x
    


