import sys
sys.path.append("../")

from core import pointArmBasedOnQuad, walk, walkWithDirection

NAO_IP = "192.168.171.80"  # Replace with the actual IP address of your Nao robot

walkWithDirection(NAO_IP, "perpleft")


