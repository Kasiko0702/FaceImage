'''
History

1.
Rev 3. add picture function for show the detect picture.
'''


'''
prepare phtot for for resize photo

'''

#def makeFace(facename, msg, endstr):
def makeFace(facename,savename,msg): #從圖片取出人臉
	#ledState =1
	if (msg != ""): #抓login in
		print(msg)  #顯示提示訊息
		with picamera.PiCamera() as camera:
			camera.resolution = (640,480)
			#camera.resolution = (320,240)
			camera.start_preview()
			# Camera warm-up time
			time.sleep(2)
			camera.capture(facename)

			image = cv2.imread(facename)  #讀檔做人臉偵測 不論login or reconigze
			gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
			faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(150,150), flags = cv2.CASCADE_SCALE_IMAGE)
			while (len(faces) ==0 ):
				print("No Face Detected")

				camera.start_preview()
				time.sleep(2)
				camera.capture(facename)
				image = cv2.imread(facename)  #讀檔做人臉偵測 不論login or reconigze
				gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
				faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(150,150), flags = cv2.CASCADE_SCALE_IMAGE)

	else:
		image = cv2.imread(facename)  #讀檔做人臉偵測 不論login or reconigze
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(150,150), flags = cv2.CASCADE_SCALE_IMAGE)


	(x, y, w, h) = (faces[0][0], faces[0][1], faces[0][2], faces[0][3])  #只取第一張人臉


	roi_color = image[y:y+h, x:x+w]#擷取人臉    

	if (h<200 or w <200):
		img2 = cv2.resize(roi_color, (200,200), interpolation = cv2.INTER_AREA)
	else:
		img2 = cv2.resize(roi_color, (200,200), interpolation = cv2.INTER_CUBIC)
                    
	cv2.imwrite(savename, img2)


def sendImageToLine(filename):

	line_bot_api = LineBotApi('rX1QsTs/XC/H+0ZpQwInN4UOayHk88FlvOzO4DPUywl5nR9XnVUp8rv8d0ouBZ9G69oegDqdCnyjS2YG9FhBd2w8AP6Q21mO2qQHkk7uVhlJqqBpjVn6oe3qYtG2N40lZOxJaAo9zIBCodtIAbJEYgdB04t98/1O/w1cDnyilFU=')

	line_bot_api.push_message('U400000041dd10ef2b036cb0325cad0c5',ImageSendMessage(original_content_url='https://ac007af2.ngrok.io/loginface.jpg',preview_image_url='https://ac007af2.ngrok.io/l.jpg'))



# main program start here
# Please use tab's.
from picamera.array import PiRGBArray
import picamera
import time
import cv2, os, math, operator
from functools import reduce
import sys
import matplotlib.pyplot as plt
#import RPi.GPIO as GPIO
#import http.client
from PIL import Image
from linebot import LineBotApi
from linebot.models import ImageSendMessage


#from PIL import Image


faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

loginname = "loginface.jpg" #登入者人臉檔案


#time.sleep(0.1) # Camera warm up
while True:

	makeFace(loginname, "l.jpg", "will take a photo")  #建立登入者人臉檔案


	sendImageToLine("l.jpg")
	time.sleep(5) # Camera warm up









