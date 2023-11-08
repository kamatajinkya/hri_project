import qi
import time
from naoqi import ALProxy

robotIP = "128.237.240.93"
port = 9559

session = qi.Session()
session.connect("tcp://" + robotIP + ":" + str(port))

tts = ALProxy("ALTextToSpeech", robotIP, port)
tts.say("turn 270 degrees")
