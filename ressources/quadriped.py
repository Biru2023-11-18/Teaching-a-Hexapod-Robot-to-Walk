import pybullet as p
import numpy as np
import os


class Hexapod:
    def __init__(self, client):
        self.client = client
        f_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'urdf/hexapod/urdf/T12.URDF')
        self.hexapodId = p.loadURDF(fileName=f_name, basePosition=[0, 0, 0.1], physicsClientId=self.client)
        self.num_joints = p.getNumJoints(self.hexapodId)
        self.joints_limit = self._get_joints_limits()


    def get_ids(self):
        return self.client, self.hexapodId

    def apply_action(self, action):
        pass

    def get_observation(self, agentId, client):
        pos, ori = p.getBasePositionAndOrientation(agentId, physicsClientId=client)
        linear_velocity, angular_velocity = p.getBaseVelocity(agentId, physicsClientId=client)

        base_state = np.concatenate([pos, ori, linear_velocity, angular_velocity])

        joint_states = [p.getJointState(self.hexapodId, i, physicsClientId=client) for i in range(self.num_joints)]
        joint_positions = [s[0] for s in joint_states]
        joint_velocity = [s[1] for s in joint_states]

        observation = np.concatenate([joint_positions, joint_velocity, base_state])

        return observation.astype(np.float32)

    def _get_joints_limits(self):
        num_joints = self.num_joints
        joints_limits = []
        for i in range(num_joints):
            info = p.getJointInfo(self.hexapodId, i)
            lower, upper = info[8], info[9]
            joints_limits.append((lower, upper))

        return joints_limits

    def denormalize_action(self, actions):
        real_angles = []
        for i, a in enumerate(actions):
            low, high = self.joints_limit[i]
            real_angle = low + (a + 1) * (high - low) /2
            real_angles.append(real_angle)
        return real_angles

