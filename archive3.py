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


num_of_joints = p.getNumJoints(robotId)
print(f'number of joints:', num_of_joints)
for i in range(num_of_joints):
    joint_info = p.getJointInfo(robotId, i)
    print(joint_info[0], ":", joint_info[1], "limits: ", joint_info[8], ":", joint_info[9] )



# # degree
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
    user_ap_angle_3 = p.readUserDebugParameter(ap_angle_1)
    user_ar_angle_3 = p.readUserDebugParameter(ar_angle_1)
    user_hp_angle_3 = p.readUserDebugParameter(hp_angle_1)
    user_hy_angle_3 = p.readUserDebugParameter(hy_angle_1)
    user_kp_angle_3 = p.readUserDebugParameter(kp_angle_1)
    user_kr_angle_3 = p.readUserDebugParameter(kr_angle_1)

    # 4
    user_ap_angle_4 = p.readUserDebugParameter(ap_angle_1)
    user_ar_angle_4 = p.readUserDebugParameter(ar_angle_1)
    user_hp_angle_4 = p.readUserDebugParameter(hp_angle_1)
    user_hy_angle_4 = p.readUserDebugParameter(hy_angle_1)
    user_kp_angle_4 = p.readUserDebugParameter(kp_angle_1)
    user_kr_angle_4 = p.readUserDebugParameter(kr_angle_1)

    # 5
    user_ap_angle_5 = p.readUserDebugParameter(ap_angle_1)
    user_ar_angle_5 = p.readUserDebugParameter(ar_angle_1)
    user_hp_angle_5 = p.readUserDebugParameter(hp_angle_1)
    user_hy_angle_5 = p.readUserDebugParameter(hy_angle_1)
    user_kp_angle_5 = p.readUserDebugParameter(kp_angle_1)
    user_kr_angle_5 = p.readUserDebugParameter(kr_angle_1)

    # 6
    user_ap_angle_6 = p.readUserDebugParameter(ap_angle_6)
    user_ar_angle_6 = p.readUserDebugParameter(ar_angle_6)
    user_hp_angle_6 = p.readUserDebugParameter(hp_angle_6)
    user_hy_angle_6 = p.readUserDebugParameter(hy_angle_6)
    user_kp_angle_6 = p.readUserDebugParameter(kp_angle_6)
    user_kr_angle_6 = p.readUserDebugParameter(kr_angle_6)


    # for j in range(num_of_joints):

    p.setJointMotorControl2(
        bodyUniqueId=robotId,
        jointIndex=0,
        controlMode=p.POSITION_CONTROL,
        targetPosition=user_hy_angle_1,
    )
    p.setJointMotorControl2(
        bodyUniqueId=robotId,
        jointIndex=1,
        controlMode=p.POSITION_CONTROL,
        targetPosition=user_hp_angle_1,
    )
    p.setJointMotorControl2(
        bodyUniqueId=robotId,
        jointIndex=2,
        controlMode=p.POSITION_CONTROL,
        targetPosition=user_kp_angle_1,
    )
    p.setJointMotorControl2(
        bodyUniqueId=robotId,
        jointIndex=3,
        controlMode=p.POSITION_CONTROL,
        targetPosition=user_kr_angle_1,
    )
    p.setJointMotorControl2(
        bodyUniqueId=robotId,
        jointIndex=4,
        controlMode=p.POSITION_CONTROL,
        targetPosition=user_ap_angle_1,
    )
    p.setJointMotorControl2(
        bodyUniqueId=robotId,
        jointIndex=5,
        controlMode=p.POSITION_CONTROL,
        targetPosition=user_ar_angle_1,
    )

    p.setJointMotorControl2(
        bodyUniqueId=robotId,
        jointIndex=6,
        controlMode=p.POSITION_CONTROL,
        targetPosition=user_hy_angle_2,
    )
    p.setJointMotorControl2(
        bodyUniqueId=robotId,
        jointIndex=7,
        controlMode=p.POSITION_CONTROL,
        targetPosition=user_hp_angle_2,
    )
    p.setJointMotorControl2(
        bodyUniqueId=robotId,
        jointIndex=8,
        controlMode=p.POSITION_CONTROL,
        targetPosition=user_kp_angle_2,
    )
    p.setJointMotorControl2(
        bodyUniqueId=robotId,
        jointIndex=9,
        controlMode=p.POSITION_CONTROL,
        targetPosition=user_kr_angle_2,
    )
    p.setJointMotorControl2(
        bodyUniqueId=robotId,
        jointIndex=10,
        controlMode=p.POSITION_CONTROL,
        targetPosition=user_ap_angle_2,
    )
    p.setJointMotorControl2(
        bodyUniqueId=robotId,
        jointIndex=11,
        controlMode=p.POSITION_CONTROL,
        targetPosition=user_ar_angle_2,
    )

    p.setJointMotorControl2(
        bodyUniqueId=robotId,
        jointIndex=12,
        controlMode=p.POSITION_CONTROL,
        targetPosition=user_hy_angle_3,
    )
    p.setJointMotorControl2(
        bodyUniqueId=robotId,
        jointIndex=13,
        controlMode=p.POSITION_CONTROL,
        targetPosition=user_hp_angle_3,
    )
    p.setJointMotorControl2(
        bodyUniqueId=robotId,
        jointIndex=14,
        controlMode=p.POSITION_CONTROL,
        targetPosition=user_kp_angle_3,
    )
    p.setJointMotorControl2(
        bodyUniqueId=robotId,
        jointIndex=15,
        controlMode=p.POSITION_CONTROL,
        targetPosition=user_kr_angle_3,
    )
    p.setJointMotorControl2(
        bodyUniqueId=robotId,
        jointIndex=16,
        controlMode=p.POSITION_CONTROL,
        targetPosition=user_ap_angle_3,
    )
    p.setJointMotorControl2(
        bodyUniqueId=robotId,
        jointIndex=17,
        controlMode=p.POSITION_CONTROL,
        targetPosition=user_ar_angle_3,
    )

    p.setJointMotorControl2(
        bodyUniqueId=robotId,
        jointIndex=18,
        controlMode=p.POSITION_CONTROL,
        targetPosition=user_hy_angle_4,
    )
    p.setJointMotorControl2(
        bodyUniqueId=robotId,
        jointIndex=19,
        controlMode=p.POSITION_CONTROL,
        targetPosition=user_hp_angle_4,
    )
    p.setJointMotorControl2(
        bodyUniqueId=robotId,
        jointIndex=20,
        controlMode=p.POSITION_CONTROL,
        targetPosition=user_kp_angle_4,
    )
    p.setJointMotorControl2(
        bodyUniqueId=robotId,
        jointIndex=21,
        controlMode=p.POSITION_CONTROL,
        targetPosition=user_kr_angle_4,
    )
    p.setJointMotorControl2(
        bodyUniqueId=robotId,
        jointIndex=21,
        controlMode=p.POSITION_CONTROL,
        targetPosition=user_kr_angle_4,
    )
    p.setJointMotorControl2(
        bodyUniqueId=robotId,
        jointIndex=22,
        controlMode=p.POSITION_CONTROL,
        targetPosition=user_ap_angle_4,
    )
    p.setJointMotorControl2(
        bodyUniqueId=robotId,
        jointIndex=23,
        controlMode=p.POSITION_CONTROL,
        targetPosition=user_ar_angle_4,
    )

    p.setJointMotorControl2(
        bodyUniqueId=robotId,
        jointIndex=24,
        controlMode=p.POSITION_CONTROL,
        targetPosition=user_hy_angle_5,
    )
    p.setJointMotorControl2(
        bodyUniqueId=robotId,
        jointIndex=25,
        controlMode=p.POSITION_CONTROL,
        targetPosition=user_hp_angle_5,
    )
    p.setJointMotorControl2(
        bodyUniqueId=robotId,
        jointIndex=26,
        controlMode=p.POSITION_CONTROL,
        targetPosition=user_kp_angle_5,
    )
    p.setJointMotorControl2(
        bodyUniqueId=robotId,
        jointIndex=27,
        controlMode=p.POSITION_CONTROL,
        targetPosition=user_kr_angle_5,
    )
    p.setJointMotorControl2(
        bodyUniqueId=robotId,
        jointIndex=28,
        controlMode=p.POSITION_CONTROL,
        targetPosition=user_ap_angle_5,
    )
    p.setJointMotorControl2(
        bodyUniqueId=robotId,
        jointIndex=29,
        controlMode=p.POSITION_CONTROL,
        targetPosition=user_ar_angle_5,
    )

    p.setJointMotorControl2(
        bodyUniqueId=robotId,
        jointIndex=30,
        controlMode=p.POSITION_CONTROL,
        targetPosition=user_hy_angle_6,
    )
    p.setJointMotorControl2(
        bodyUniqueId=robotId,
        jointIndex=31,
        controlMode=p.POSITION_CONTROL,
        targetPosition=user_hp_angle_6,
    )
    p.setJointMotorControl2(
        bodyUniqueId=robotId,
        jointIndex=32,
        controlMode=p.POSITION_CONTROL,
        targetPosition=user_kp_angle_6,
    )
    p.setJointMotorControl2(
        bodyUniqueId=robotId,
        jointIndex=33,
        controlMode=p.POSITION_CONTROL,
        targetPosition=user_kr_angle_6,
    )
    p.setJointMotorControl2(
        bodyUniqueId=robotId,
        jointIndex=34,
        controlMode=p.POSITION_CONTROL,
        targetPosition=user_ap_angle_6,
    )
    p.setJointMotorControl2(
        bodyUniqueId=robotId,
        jointIndex=35,
        controlMode=p.POSITION_CONTROL,
        targetPosition=user_ar_angle_6,
    )

    p.stepSimulation()
    # time.sleep(1. / 240.)