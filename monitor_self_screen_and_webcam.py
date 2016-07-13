import os
import time
import cv2

cpt = 0
maxFrames = 2 # if you want 5 frames only.

try:
    vidStream = cv2.VideoCapture(0) # index of your camera
except:
    print "problem opening input stream"
    sys.exit(1)

while cpt < maxFrames:
	timestr = time.strftime("%Y%m%d-%H%M%S")
	print timestr
	os.system(("screencapture -x %s.jpg") % (timestr))
	ret, frame = vidStream.read() # read frame and return code.
	if not ret: # if return code is bad, abort.
		sys.exit(0)
	#cv2.imshow("test window", frame) # show image in window
	#cv2.imwrite("image%04i.jpg" %cpt, frame)
	cv2.imwrite("%s_me.jpg" %timestr, frame)
	os.system(("convert %s.jpg -resize 1024X768 -quality 50 %s.jpg") % (timestr,timestr))
	os.system(("convert %s_me.jpg -resize 1024X768 -quality 50 %s_me.jpg") % (timestr,timestr))
	os.system(("convert +append %s.jpg %s_me.jpg %s_me_screen.jpg") % (timestr,timestr,timestr))
	os.system(("convert %s_me_screen.jpg -resize 1024x768 %s_me_screen.jpg") % (timestr,timestr))
	cpt += 1
	time.sleep(1)

del(vidStream)





