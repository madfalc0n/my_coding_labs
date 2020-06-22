import gym
import numpy as np

env = gym.make('MountainCar-v0')
env.reset()

print(env.observation_space.high)
print(env.observation_space.low)
print(env.action_space.n)

DISCRETE_OS_SIZE = [20] * len(env.observation_space.high)
print(DISCRETE_OS_SIZE)

discrete_os_win_size = (env.observation_space.high-env.observation_space.low) / DISCRETE_OS_SIZE

print(discrete_os_win_size)

q_table = np.random.uniform(low=-2, high=0, size = (DISCRETE_OS_SIZE + [env.action_space.n]))
#print(q_table)
#print(len(q_table))
print(q_table.shape)

# done = False

# while not done:
#     action = 2
#     new_state, reward, donem, _ = env.step(action)
#     print(f"reward : {reward} new_state : {new_state}")
#     env.render()

# env.close()