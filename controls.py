import math

import pybullet as p, pybullet_data, time
import numpy as np

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.81)

# p.configureDebugVisualizer(p.COV_ENABLE_WIREFRAME, 1)
# p.configureDebugVisualizer(p.COV_ENABLE_GUI, 1)

p.loadURDF("plane.urdf", [0, 0, 0], [0, 0, 0, 1])

orn = p.getQuaternionFromEuler([math.pi, 0, 0])
# orn = p.getQuaternionFromEuler([0, 0, 0])


robot = p.loadURDF("ressources/urdf/hexapod/urdf/T12.URDF", basePosition=[0,0,0.5], baseOrientation=orn)
# robot = p.loadURDF("ressources/urdf/mini_cheetah/urdf/mini_cheetah.urdf", basePosition=[0,0,0.33])

print("Num joints:", p.getNumJoints(robot))
pos, orn = p.getBasePositionAndOrientation(robot)
euler = p.getEulerFromQuaternion(orn)
print("base euler (rad):", euler)
# linkIndex = -1 is base
link_state = p.getLinkState(robot, 0)
print(f"link 0 state: ",link_state)


# total mass from dynamics
total_mass = 0.0
for i in range(-1, p.getNumJoints(robot)):
    total_mass += p.getDynamicsInfo(robot, i)[0]
print("Total mass (from dynamics):", total_mass)

neutral_pose = [
    0, 0.52, 1.6, 0, -0.52, 0,
    0, 0.52, 1.6, 0, -0.52, 0,
    0, 0.52, 1.6, 0, -0.52, 0,
    0, 0.52, 1.6, 0, -0.52, 0,
    0, 0.52, 1.6, 0, -0.52, 0,
    0, 0.52, 1.6, 0, -0.52, 0,
]
for i, pose in enumerate(neutral_pose):
    p.setJointMotorControl2(
        bodyUniqueId=robot,
        jointIndex=i,
        controlMode=p.POSITION_CONTROL,
        targetPosition=pose,
        force=0
    )

# robot.appyAction(neutral_pose)

# for j in range(p.getNumJoints(robot)):
#     p.setJointMotorControl2(
#         bodyUniqueId=robot,
#         jointIndex=j,
#         controlMode=p.POSITION_CONTROL,
#         targetPosition=0,
#         force=600
#     )
# set a modest target for joint 0
# p.setJointMotorControl2(robot, 0, p.POSITION_CONTROL, targetPosition=0.2, force=10000)
for _ in range(24000):
    p.stepSimulation()
    time.sleep(1/240)
