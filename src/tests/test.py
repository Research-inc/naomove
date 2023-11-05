import sys
sys.path.append("../")

from core import pointArm

NAO_IP = "192.168.171.80"  # Replace with the actual IP address of your Nao robot

pointArm(NAO_IP, "RArm", 0)

pointArm(NAO_IP, "LArm", 0)
