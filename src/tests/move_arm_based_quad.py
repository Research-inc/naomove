import sys
sys.path.append("../")

from core import pointArmBasedOnQuad

NAO_IP = "192.168.171.80"  # Replace with the actual IP address of your Nao robot

pointArmBasedOnQuad(NAO_IP, "first", 0.0)

pointArmBasedOnQuad(NAO_IP, "second", 0.0)

pointArmBasedOnQuad(NAO_IP, "third", 0.0)

pointArmBasedOnQuad(NAO_IP, "fourth", 0.0)
