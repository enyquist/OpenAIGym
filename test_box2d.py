"""
Script for testing that the advanced options for OpenAI Gym was installed correctly. Output should render the
Bipedal Walker environment
"""

import gym

env = gym.make('BipedalWalker-v3')
env.reset()

for _ in range(1000):
    env.render()
    env.step(env.action_space.sample())
