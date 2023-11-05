# -*- encoding: UTF-8 -*-
import math
import sys
import time
from naoqi import ALProxy

def pointArm(NAO_IP, arm="RArm", angle=0.0):
    motion = ALProxy("ALMotion", NAO_IP, 9559)

    try:
        # Set the stiffness of the arm and head
        motion.stiffnessInterpolation(arm, 1.0, 1.0)

        # Raise the arm (pointing gesture)
        target_angle = math.radians(angle)  # Adjust the angles as needed
        speed = 0.2  # Adjust the speed as needed

        motion.angleInterpolation(arm, target_angle, speed, True)

        # Wait for a moment to see the pointing gesture
        time.sleep(3)

        # Lower the arm to its initial position
        initial_angle = 0.0  # Adjust the angles as needed
        motion.angleInterpolation(arm, initial_angle, speed, True)

    except KeyboardInterrupt:
        pass
    finally:
        # Release stiffness at the end
        motion.stiffnessInterpolation(arm, 0.0, 1.0)

def pointArmBasedOnQuad(NAO_IP, quad="first", angle=0.0):
    arm = "LArm"
    if quad == "first" or quad == "second":
        arm = "RArm"
    pointArm(NAO_IP, arm, angle)