import qi
import time
from naoqi import ALProxy

robotIP = "128.237.247.249"
port = 9559

session = qi.Session()
session.connect("tcp://" + robotIP + ":" + str(port))

motion_service = session.service("ALMotion")
posture_service = session.service("ALRobotPosture")

posture_service.goToPosture("StandInit", 0.5)

motion_service.setAngles("LShoulderPitch", 0.0, 0.1)
time.sleep(2)
motion_service.openHand("LHand")
motion_service.closeHand("LHand")
motion_service.closeHand("LHand")
