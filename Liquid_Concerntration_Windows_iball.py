import cv2
import time

def rescale_frame(frame, percent=80):  # make the video windows a bit smaller
            width = int(frame.shape[1] * percent / 100)
            height = int(frame.shape[0] * percent / 100)
            dim = (width, height)
            return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
        
def Colour_Concentration(frame):
    while cap.isOpened():
        ret, frame = cap.read()
        print("Colour Concentration")
        try: 
            text = ""
            frame = rescale_frame(frame)
            out_new = np.uint8(frame)
            out_Gray = cv2.cvtColor(out_new, cv2.COLOR_BGR2GRAY)
            ret, thresh_out = cv2.threshold(out_Gray, 127, 255, cv2.THRESH_BINARY_INV)
            kernel_ip = np.ones((2, 2), np.uint8)
            eroded_ip = cv2.erode(thresh_out, kernel_ip, iterations=1)
            dilated_ip = cv2.dilate(eroded_ip, kernel_ip, iterations=1)
            #             cv2.imshow("testing 222", dilated_ip)
            cnts = cv2.findContours(dilated_ip.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)

            if len(cnts) == 0:
            flag_empty = 1

            flag_detected = 0
            #         text = "Empty Frame"
            #         cv2.putText(frame, text, (25,25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255),2)
            cv2.imshow("output", frame)
            cv2.waitKey(30)
            # converting  BGR to HSV Frame
            Big_faulty = max(cnts, key=cv2.contourArea)
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            # the range of red color
            blu_lower = np.array([105, 142, 164], np.uint8)
            blu_upper = np.array([111, 232, 213], np.uint8)

            # finding the range of red color in the image
            red = cv2.inRange(hsv, blu_lower, blu_upper)
            kernal = np.ones((3, 3), "uint8")

            # dilation of the image ( to remove noise) create mask for red color
            red = cv2.dilate(red, kernal, iterations=1)
            res = cv2.bitwise_and(frame, frame, mask=red)

            contours, hierarchy = cv2.findContours(red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            if len(contours) != 0:
            Big_Con = max(contours, key=cv2.contourArea)
            if (cv2.contourArea(Big_Con) > 5000):
                x, y, w, h = cv2.boundingRect(Big_Con)
                frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                if (x > 10 & x < 420):
                    text = "concentration is good"
            # elif (cv2.contourArea(Big_faulty) > 4000):
            else:
                x, y, w, h = cv2.boundingRect(Big_faulty)
                frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                if (x > 10 & x < 420):
                    if (text == "concentration is good"):
                        text = "concentration is good"
                    else:
                        text = "concentration is too high"
            cv2.putText(frame, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
            cv2.imshow("output", frame)
        except:
      
if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    Colour_Concentration(frame)
        
