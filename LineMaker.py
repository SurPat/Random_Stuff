import cv2


def patt1(frame,length,width):
	H_Strtpt=(int(length/2),0)
	H_Stppt=(int(length/2),width)
	cv2.line(frame, H_Strtpt, H_Stppt,(0,0,255),2)
	V_Strtpt = (0,int(width/2))
	V_Stppt = (length,int(width/2))
	cv2.line(frame, V_Strtpt, V_Stppt,(0,0,255), 2)
	cv2.imshow('check', frame)

def patt2(frame,length,width):
	for i in range(1,4):
		V_Strtpt = (i*160,0)
		V_Stppt = (i*160,length)
		cv2.line(frame, V_Strtpt, V_Stppt,(0,0,255), 2)
		cv2.imshow('check', frame)


def quad(frame,patt):
		ret, frame = cap.read()
		cv2.imshow('check', frame)
		width,length, __ = frame.shape
		print(length,width)
		if patt==1:
			patt1(frame,length,width)
		if patt==2:
			patt2(frame,length,width)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
