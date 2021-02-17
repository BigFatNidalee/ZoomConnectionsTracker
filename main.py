from desktopmagic.screengrab_win32 import (
	getDisplayRects, saveScreenToBmp, saveRectToBmp, getScreenAsImage,
	getRectAsImage, getDisplaysAsImages)
from playsound import playsound
import cfg
import pytesseract

pytesseract.pytesseract.tesseract_cmd = cfg.tesseractInstallLocation
membersOnline = 0


def getMembers():
	img = getRectAsImage(cfg.membersCountPos)
	txt = pytesseract.image_to_string(img)
	members = int(''.join(i for i in txt if i.isdigit()))
	return members


def compareMembers(newValue):
	global membersOnline
	if newValue > membersOnline:
		playsound("joined.mp3")
		membersOnline = newValue
	else:
		if newValue < membersOnline:
			playsound("left.mp3")
			membersOnline = newValue


while True:
	compareMembers(getMembers())
