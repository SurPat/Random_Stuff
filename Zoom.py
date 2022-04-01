import math
import cv2

#=============================== global Variables ====================================#
crop = False
cropped_img = None ; zoomop = False
crp_a,crp_b = None, None ; crp_c,crp_d = None, None
scale = 7
points = []
#=============================== Image Loading ====================================#
img = cv2.imread("Island.jpeg")
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

#=============================== Event Method ====================================#
def cropping(event, x, y, flags, param):
    global crp_a, crp_b, crp_c, crp_d, scale, crop, cropped_img, img, zoomop
    global points
    if event == cv2.EVENT_RBUTTONDOWN:
        global crp_a, crp_b, crp_c, crp_d, scale, crop, cropped_img, img
        crp_a, crp_b = x, y
        print("X, y value: ", x, y)
    if event == cv2.EVENT_RBUTTONUP:
        try:
            cropped_img = img[crp_b:y,crp_a:x]
            cx,cy,__ = cropped_img.shape
            cx,cy = int(cx*scale),int(cy*scale)
            cropped_img = cv2.resize(cropped_img,(cy,cx))
            zoomop = True
            cv2.imshow("cropImage", cropped_img)
            cv2.namedWindow("cropImage")
            cv2.setMouseCallback('cropImage', cropping)
        except:
            print("Zoom operation out")
    if event == cv2.EVENT_RBUTTONDBLCLK:
        zoomop = False
    if event == cv2.EVENT_LBUTTONDOWN and zoomop:
        print("Here, Cropped Image Coordinates: ", crp_a, crp_b)
        cv2.circle(img, (crp_a + int(x/scale),crp_b + int(y/scale)), 1, (0, 0, 255), 1)
    if event == cv2.EVENT_LBUTTONDOWN and zoomop:
        points.append((x,y))
        if len(points) == 1:
            cv2.circle(img, (crp_a + int(x/scale),crp_b + int(y/scale)), 1, (0, 0, 255), 1)
            cv2.putText(img,"(0,0)",(crp_a + int(x/scale)+1, crp_b + int(y/scale)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0),2)
            print("Latest List of points: ", points)
        elif len(points)>2:
            cv2.circle(img, (crp_a + int(x/scale),crp_b + int(y/scale)), 1, (0, 0, 255), 1)
            cv2.line(img,points[0],(crp_a + int(x/scale),crp_b + int(y/scale)),(0, 255, 255))
            distance = math.dist(points[0], points[-1])
            cv2.putText(img, str(round(distance,2)), (crp_a + int(x/scale)+10,crp_b + int(y/scale)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
            print("Latest List of points: ", points)
    if event == cv2.EVENT_LBUTTONDOWN and zoomop == False:
        points.append((x,y))
        if len(points) == 1:
            cv2.circle(img, (x, y), 1, (0, 0, 255), 1)
            cv2.putText(img,"(0,0)",(x+1, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0),2)
            print("Latest List of points: ", points)
        elif len(points) >= 2:
            cv2.circle(img, (x, y), 1, (0, 0, 255), 1)
            cv2.line(img, points[0], points[-1], (0, 255, 255))
            distance = math.dist(points[0],points[-1])
            cv2.putText(img, str(round(distance,2)), (x + 1, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
            print("Latest List of points: ",points)

if __name__ == "__main__":
    cv2.imshow('image', img)
    cv2.namedWindow("image")
    cv2.setMouseCallback('image', cropping)
    while(1):
        #img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
        cv2.imshow('image', img)
        if cv2.waitKey(20) == ord('q'):
            break
    cv2.destroyAllWindows()
