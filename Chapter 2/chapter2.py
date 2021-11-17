# Chapter 2: N-armed Bandits
# Deep Reinforcement Learning in Action

import numpy as np
from scipy import stats
import random
import matplotlib.pyplot as plt

# Listing 2.1 Finding the best actions given the expected rewards in Python 3

def get_best_action(actions):
    best_action = 0
    max_action_value = 0
    for i in range(len(actions)):
        cur_action_value = get_action_value(actions[i])
        if cur_action_value > max_action_value:
            best_action =  i
            max_action_value = cur_action_value
    return best_action

# Listing 2.2 Epsilon-greedy strategy for action selection

# Number of arms
n = 10

# Hidden probabilities associated with each arm
probs = np.random.rand(n)

# Epsilon for epsilon-greedy action selection
eps = 0.1

# Listing 2.3 Defining the reward function
def get_reward(prob, n = 10):
    reward = 0
    for i in range(n):
        if random.random() < prob:
            reward += 1
    return reward

reward_test = [get_reward(0.7) for _ in range(2000)]
np.mean(reward_test)

sum = 0
x = [4, 5, 6, 7]
for j in range(len(x)):
    sum = sum + j

plt.figure(figsize=9.5)
plt.xlabel("Reward", fontsize=22)
plt.ylabel("# Observation", fontsize=22)
plt.hist(reward_test, bins=9)

