import pybullet as p
import pybullet_data
import os

class Taget:
    def __init__(self, client, base):
        f_name = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'urdf/target.urdf')
        self.target = p.loadURDF(f_name, basePosition=[base[0], base[1], base[2]],
                   physicsClientId=client)