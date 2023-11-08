from naoqi import ALProxy
import time

IP = '128.237.247.249'
motion = ALProxy("ALMotion", IP, 9559)
tts    = ALProxy("ALTextToSpeech", IP, 9559)
#motion.moveInit()
motion.moveToward(0.5, 0, 0)
#motion.wait(id, 0)
