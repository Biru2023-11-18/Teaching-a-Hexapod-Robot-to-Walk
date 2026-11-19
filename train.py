import os
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv, VecNormalize
from envs.hexapod_env import HexapodEnv

def make_env():
    def _init():
        return HexapodEnv(render=False)
    return _init

if __name__ == "__main__":
    os.makedirs("models", exist_ok=True)
    env = DummyVecEnv([make_env() for _ in range(8)])
    env = VecNormalize(env, norm_obs=True, norm_reward=True, clip_obs=10.0)

    model = PPO("MultiInputPolicy", env,
                verbose=1,
                tensorboard_log="./logs/",
                n_steps=2048,
                batch_size=256,
                learning_rate=3e-4,
                ent_coef=0.0)

    model.learn(total_timesteps=2_000_000)
    model.save("models/ppo_hexapod1000")
    env.save("models/vecnormalize1000.pkl")