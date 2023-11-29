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



def StiffnessOn(proxy):
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    pStiffnessLists = 1.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)


def walk(NAO_IP, x, y):
    # Init proxies.
    try:
        motionProxy = ALProxy("ALMotion", NAO_IP, 9559)
    except Exception, e:
        print "Could not create proxy to ALMotion"
        print "Error was: ", e

    try:
        postureProxy = ALProxy("ALRobotPosture", NAO_IP, 9559)
    except Exception, e:
        print "Could not create proxy to ALRobotPosture"
        print "Error was: ", e

    # Set NAO in Stiffness On
    StiffnessOn(motionProxy)

    # Send NAO to Pose Init
    postureProxy.goToPosture("StandInit", 0.5)

    #####################
    ## Enable arms control by Walk algorithm
    #####################
    motionProxy.setWalkArmsEnabled(True, True)
    #~ motionProxy.setWalkArmsEnabled(False, False)

    #####################
    ## FOOT CONTACT PROTECTION
    #####################
    #~ motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", False]])
    motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])


    #TARGET VELOCITY
    X = x
    Y = y
    Theta = 0.0
    Frequency =1.0 # max speed
    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)

    time.sleep(4.0)

    #TARGET VELOCITY
    #X = 0.2
    #Y = -0.5
    #Theta = 0.2
    #Frequency =1.0
    #motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)

    #time.sleep(2.0)

    #####################
    ## End Walk
    #####################
    #TARGET VELOCITY
    X = 0.0
    Y = 0.0
    Theta = 0.0
    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)

def walkWithDirection(NAO_IP, direction):

    if direction == "angleright":
        walk(NAO_IP, 0.5, -0.5)

    elif direction == "angleleft":
        walk(NAO_IP, 0.5, 0.5)

    elif direction == "left":
        walk(NAO_IP, 0, 0.5)

    elif direction == "right":
        walk(NAO_IP, 0, -0.5)