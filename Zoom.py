import cv2
import numpy as np

crop = False; cropped_img = None
crp_a,crp_b = None, None
crp_c,crp_d = None, None
scale = 7

#def crop_mark():


def cropping(event, x, y, flags, param):
    global crp_a, crp_b, crp_c, crp_d, scale, crop, cropped_img, img
    if event == cv2.EVENT_RBUTTONDOWN:
        global crp_a, crp_b, crp_c, crp_d, scale, crop, cropped_img, img
        crp_a, crp_b = x, y
        print("X, y value: ", x, y)
    if event == cv2.EVENT_RBUTTONUP:
        #cv2.rectangle(img, (crp_a, crp_b), (x, y), (255, 255, 255), 1)
        cropped_img = img[crp_b:y,crp_a:x]
        cx,cy,__ = cropped_img.shape
        cx,cy = int(cx*scale),int(cy*scale)
        cropped_img = cv2.resize(cropped_img,(cy,cx))
        cv2.imshow("cropImage", cropped_img)
        cv2.namedWindow("cropImage")
        cv2.setMouseCallback('cropImage', cropping)
    if event == cv2.EVENT_LBUTTONDOWN and scale>0:
        print("Here, Cropped Image Coordinates: ", crp_a, crp_b)
        try:
            cv2.circle(cropped_img, (x, y), 1, (0, 0, 255), 1)
            cv2.circle(img, (crp_a + int(x/scale),crp_b + int(y/scale)), 1, (0, 0, 255), 1)
        except:
            cv2.circle(cropped_img, (x, y), 1, (0, 0, 255), 1)
            cv2.circle(img, (x,y), 1, (0, 0, 255), 1)
img = cv2.imread("Island.jpeg")
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
cv2.imshow('image', img)
cv2.namedWindow("image")
cv2.setMouseCallback('image',cropping)

while(1):
    #img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
    cv2.imshow('image', img)
    if cv2.waitKey(20) == ord('q'):
        break
cv2.destroyAllWindows()