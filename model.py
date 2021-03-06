import torch
import torch.nn as nn
import torch.nn.functional as F

class QNetwork(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size, action_size, seed, fc1_units=64, fc2_units=64):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
            fc1_units (int): Number of nodes in first hidden layer
            fc2_units (int): Number of nodes in second hidden layer
        """
        super(QNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)
        self.fc1 = nn.Linear(state_size, fc1_units)
        self.fc2 = nn.Linear(fc1_units, fc2_units)
        self.fc3 = nn.Linear(fc2_units, action_size)

    def forward(self, state):
        """Build a network that maps state -> action values."""
        x = F.relu(self.fc1(state))
        x = F.relu(self.fc2(x))
        return self.fc3(x)
    
class Dueling_DQN(nn.Module):
    def __init__(self, state_size, action_size, seed, fc1_units=512, fc2_units=512):
        super(Dueling_DQN, self).__init__()
        self.action_size = action_size
        

        self.fc1_adv = nn.Linear(state_size, fc1_units)
        self.fc1_val = nn.Linear(state_size, fc1_units)

        self.fc2_adv = nn.Linear(fc1_units, action_size)
        self.fc2_val = nn.Linear(fc1_units, 1)

        self.relu = nn.ReLU()

    def forward(self, x):
        
        adv = self.relu(self.fc1_adv(x))
        val = self.relu(self.fc1_val(x))

        adv = self.fc2_adv(adv)
        val = self.fc2_val(val).expand(x.size(0), self.action_size)
        
        x = val + adv - adv.mean(1).unsqueeze(1).expand(x.size(0), self.action_size)
        return x
    
    
      


    
    