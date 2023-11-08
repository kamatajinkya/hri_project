import qi 
import time
from naoqi import ALProxy

robotIP = "128.237.247.249"
port = 9559

session = qi.Session()
session.connect("tcp://" + robotIP + ":" + str(port))

posture_service = session.service("ALRobotPosture")
basic_awareness = ALProxy("ALBasicAwareness", robotIP, port)

posture_service.goToPosture("StandInit", 0.3)
basic_awareness.startAwareness()
basic_awareness.setEngagementMode("Unengaged")

