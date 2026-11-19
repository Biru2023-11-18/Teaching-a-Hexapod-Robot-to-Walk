from stable_baselines3 import PPO

from envs.hexapod_env import HexapodEnv

env = HexapodEnv(render=True)
model = PPO.load("models/ppo_hexapod4")

obs, info = env.reset()

# for _ in range(1000):
#     action, _ = model.predict(obs, deterministic=True)
#     obs, reward, done, truncated, info = env.step(action)
#
#     if done or truncated:
#         obs, info = env.reset()

while True:
    action, _ = model.predict(obs, deterministic=True)
    obs, reward, done, truncated, info = env.step(action)

    if done or truncated:
        obs, info = env.reset()
