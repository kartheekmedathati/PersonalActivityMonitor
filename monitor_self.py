import os
import time
counter=0;
while counter<1620:
	timestr = time.strftime("%Y%m%d-%H%M%S")
	print timestr
	os.system(("screencapture -x %s.jpg") % (timestr))
	os.system(("convert %s.jpg -resize 1024X768 -quality 50 %s.jpg") % (timestr,timestr))
	time.sleep(20)


