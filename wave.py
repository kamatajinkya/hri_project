import qi
import time
from naoqi import ALProxy

robotIP = "128.237.247.249"
port = 9559

session = qi.Session()
session.connect("tcp://" + robotIP + ":" + str(port))

tts = ALProxy("ALTextToSpeech", robotIP, port)
motion_proxy = ALProxy("ALMotion", robotIP, port)

motion_service = session.service("ALMotion")
posture_service = session.service("ALRobotPosture")

posture_service.goToPosture("StandInit", 0.5)

motion_service.setAngles("RShoulderPitch", -0.25, 0.2)
motion_service.setAngles("RShoulderRoll", -0.5, 0.1)
motion_service.setAngles("RElbowRoll", 1.5, 0.1)
motion_service.setAngles("RWristYaw", -1.0, 0.1)

time.sleep(1)
motion_service.openHand("RHand")
# tts.say("hay im pepper")
motion_service.openHand("RHand")
