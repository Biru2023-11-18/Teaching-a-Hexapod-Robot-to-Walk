import numpy as np
import pybullet as p
import pybullet_data
import time

from pybullet import addUserDebugParameter

physicsClient = p.connect(p.GUI)
print(f'is Connected ? ',p.isConnected())
p.resetSimulation()
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -10)
# p.setRealtimeSimulation(0)


planeId = p.loadURDF("plane.urdf", [0, 0, 0], [0, 0, 0, 1])
startPos = [0,0,1]
startOrientation = p.getQuaternionFromEuler([0,0,0])
# robotId = p.loadURDF("r2d2.urdf",startPos, startOrientation)
robotId = p.loadURDF("ressources/urdf/hexapod/urdf/T12.URDF", basePosition=[0, 0, 0.1])

total_mass = 0.0
for i in range(-1, p.getNumJoints(robotId)):
    # -1 corresponds to base link
    mass = p.getDynamicsInfo(robotId, i)[0]
    total_mass += mass
print("Total robot mass:", total_mass)


num_of_joints = p.getNumJoints(robotId)
pos, orn = p.getBasePositionAndOrientation(robotId)
lin_vel, ang_vel = p.getBaseVelocity(robotId)
print(f'number of joints: {num_of_joints} \n position: {pos} \n orientation: {orn} \n linear velocity: {lin_vel} \n angular velocity: {ang_vel} ')


for i in range(num_of_joints):
    joint_info = p.getJointInfo(robotId, i)
    print(joint_info[0], ":", joint_info[1])

for i in range(num_of_joints):
    joint_state = p.getJointState(robotId, i)
    # print("JOINT STATE", i, ":", joint_state[0], ":", joint_state[1])
    print("JOINT STATE", i, ":", joint_state)


# degree
ap_angle_1 = p.addUserDebugParameter('AP1', -120, 120, 0)
ar_angle_1 = p.addUserDebugParameter('AR1', -180, 180, 0)
hp_angle_1 = p.addUserDebugParameter('HP1', -110, 90, 0)
hy_angle_1 = p.addUserDebugParameter('HY1', -180, 180, 0)
kp_angle_1 = p.addUserDebugParameter('KP1', -110, 180, 0)
kr_angle_1 = p.addUserDebugParameter('KR1', -180, 180, 0)

ap_angle_2 = p.addUserDebugParameter('AP2', -120, 120, 0)
ar_angle_2 = p.addUserDebugParameter('AR2', -180, 180, 0)
hp_angle_2 = p.addUserDebugParameter('HP2', -110, 90, 0)
hy_angle_2 = p.addUserDebugParameter('HY2', -180, 180, 0)
kp_angle_2 = p.addUserDebugParameter('KP2', -110, 180, 0)
kr_angle_2 = p.addUserDebugParameter('KR2', -180, 180, 0)

ap_angle_3 = p.addUserDebugParameter('AP3', -120, 120, 0)
ar_angle_3= p.addUserDebugParameter('AR3', -180, 180, 0)
hp_angle_3= p.addUserDebugParameter('HP3', -110, 90, 0)
hy_angle_3= p.addUserDebugParameter('HY3', -180, 180, 0)
kp_angle_3= p.addUserDebugParameter('KP3', -110, 180, 0)
kr_angle_3= p.addUserDebugParameter('KR3', -180, 180, 0)

ap_angle_4= p.addUserDebugParameter('AP4', -120, 120, 0)
ar_angle_4 = p.addUserDebugParameter('AR4', -180, 180, 0)
hp_angle_4 = p.addUserDebugParameter('HP4', -110, 90, 0)
hy_angle_4 = p.addUserDebugParameter('HY4', -180, 180, 0)
kp_angle_4 = p.addUserDebugParameter('KP4', -110, 180, 0)
kr_angle_4 = p.addUserDebugParameter('KR4', -180, 180, 0)

ap_angle_5 = p.addUserDebugParameter('AP5', -120, 120, 0)
ar_angle_5 = p.addUserDebugParameter('AR5', -180, 180, 0)
hp_angle_5 = p.addUserDebugParameter('HP5', -110, 90, 0)
hy_angle_5 = p.addUserDebugParameter('HY5', -180, 180, 0)
kp_angle_5 = p.addUserDebugParameter('KP5', -110, 180, 0)
kr_angle_5 = p.addUserDebugParameter('KR5', -180, 180, 0)

ap_angle_6 = p.addUserDebugParameter('AP6', -120, 120, 0)
ar_angle_6 = p.addUserDebugParameter('AR6', -180, 180, 0)
hp_angle_6 = p.addUserDebugParameter('HP6', -110, 90, 0)
hy_angle_6 = p.addUserDebugParameter('HY6', -180, 180, 0)
kp_angle_6 = p.addUserDebugParameter('KP6', -110, 180, 0)
kr_angle_6 = p.addUserDebugParameter('KR6', -180, 180, 0)



# radians

# ap_angle = addUserDebugParameter('AP', -2.1, 2.1, 0)
# ar_angle = addUserDebugParameter('AR', -3.1, 3.1, 0)
# hp_angle = addUserDebugParameter('HP', -1.9, 1.6, 0)
# hy_angle = addUserDebugParameter('HY', -3.1, 3.1, 0)
# kp_angle = addUserDebugParameter('KP', -1.9, 3.1, 0)
# kr_angle = addUserDebugParameter('KR', -3.1, 3.1, 0)

# for _ in range(10000):
#     pos , ori = p.getBasePositionAndOrientation(robotId)
#     # p.applyExternalForce(robotId, 0, [50, 0, 0], [0, 0 ,0], p.WORLD_FRAME)
#
#     p.stepSimulation()

while True:

    # 1
    user_ap_angle_1 = p.readUserDebugParameter(ap_angle_1)
    user_ar_angle_1 = p.readUserDebugParameter(ar_angle_1)
    user_hp_angle_1 = p.readUserDebugParameter(hp_angle_1)
    user_hy_angle_1 = p.readUserDebugParameter(hy_angle_1)
    user_kp_angle_1 = p.readUserDebugParameter(kp_angle_1)
    user_kr_angle_1 = p.readUserDebugParameter(kr_angle_1)

    # 2
    user_ap_angle_2 = p.readUserDebugParameter(ap_angle_2)
    user_ar_angle_2 = p.readUserDebugParameter(ar_angle_2)
    user_hp_angle_2 = p.readUserDebugParameter(hp_angle_2)
    user_hy_angle_2 = p.readUserDebugParameter(hy_angle_2)
    user_kp_angle_2 = p.readUserDebugParameter(kp_angle_2)
    user_kr_angle_2 = p.readUserDebugParameter(kr_angle_2)
    # 3

    # 4

    # 5

    # 6
    user_ap_angle_6 = p.readUserDebugParameter(ap_angle_6)
    user_ar_angle_6 = p.readUserDebugParameter(ar_angle_6)
    user_hp_angle_6 = p.readUserDebugParameter(hp_angle_6)
    user_hy_angle_6 = p.readUserDebugParameter(hy_angle_6)
    user_kp_angle_6 = p.readUserDebugParameter(kp_angle_6)
    user_kr_angle_6 = p.readUserDebugParameter(kr_angle_6)

    # for joint_index in range(num_of_joints):
    # p.setJointMotorControl2(
    #     bodyUniqueId=robotId,
    #     jointIndex=0,
    #     controlMode=p.POSITION_CONTROL,
    #     targetPosition=user_angle,
    # )
    p.setJointMotorControl2(
        bodyUniqueId=robotId,
        jointIndex = 1,
        controlMode=p.POSITION_CONTROL,
        targetPosition=user_ap_angle_1,
    )
    p.stepSimulation()