import time
import gym
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv, VecNormalize
from envs.hexapod_env import HexapodEnv

if __name__ == "__main__":
    env = DummyVecEnv([lambda: HexapodEnv(render=True)])
    # load normalization if used during training
    try:
        env = VecNormalize.load("models/vecnormalize.pkl", env)
        env.training = False
        env.norm_reward = False
    except Exception:
        pass

    model = PPO.load("models/ppo_hexapod")
    obs = env.reset()
    for _ in range(10000):
        action, _ = model.predict(obs, deterministic=True)
        obs, reward, done, info = env.step(action)
        env.render()
        time.sleep(1/60.0)
        if done:
            obs = env.reset()