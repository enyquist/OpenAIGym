"""
Script for testing that OpenAI Gym was installed correctly. Output should render the Mountain Car environment
"""

import gym

env = gym.make('MountainCar-v0')
env.reset()

for _ in range(2000):
    env.render()
    env.step(env.action_space.sample())  # Send a random action
