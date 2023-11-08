import qi
import time
from naoqi import ALProxy

IP = "128.237.247.249"
PORT = 9559

tts = ALProxy("ALTextToSpeech", IP, int(PORT))
#tts.say("mai hu don")

session = qi.Session()
try:
    session.connect('tcp://' + IP + ':' + str(PORT))
except:
    raise Exception('connect nahi hua')


motion_service = session.service("ALMotion")
motion_service.wakeUp()
motion_service.moveTo(1.0, -1.0, 0.0)
time.sleep(5)
