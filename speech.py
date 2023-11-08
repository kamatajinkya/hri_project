import qi
import time
from naoqi import ALProxy

robotIP = "128.237.247.249"
port = 9559

session = qi.Session()
session.connect("tcp://" + robotIP + ":" + str(port))

tts = ALProxy("ALTextToSpeech", robotIP, port)
tts.setParameter("speed", 20000)
tts.say("Hello Olivia and Ajinkya how are you today?")
tts.say("Is there anything I can help you with during your time here?")
# tts.say("make a 270 digree turn clockwise, take 150 tiny steps, make your way towards the three people you see, hint, they may or may not be real, so look carefully, then, pass yourself on the right 2 times, go north west, walk for 2 or 3 seconds, open the door")
