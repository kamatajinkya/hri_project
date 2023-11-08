import qi 
import time
from naoqi import ALProxy

robotIP = "128.237.247.249"
port = 9559

session = qi.Session()
session.connect("tcp://" + robotIP + ":" + str(port))

motion_proxy = ALProxy("ALMotion", robotIP, port)

motion_service = session.service("ALMotion")
posture_service = session.service("ALRobotPosture")

# rotate
# 7.1s : rotation - 2pi
# 3.75s : rotation - pi
motion_proxy.moveToward(0.0, 0.0, 1.0)
time.sleep(3.75)

motion_proxy.stopMove()
