import pypylon.pylon as py
import numpy as np
import time 
import cv2

class BaslerCam:

    def initiate(self,dev_num):
    # Simply get the first available pylon device.
        first_device = py.TlFactory.GetInstance().CreateFirstDevice()
        instant_camera = py.InstantCamera(first_device)
        instant_camera.Open()
        # Optional if you set it in Pylon Viewer
        instant_camera.PixelFormat = "BayerRG8"
        instant_camera.StartGrabbing(py.GrabStrategy_LatestImages)
        return instant_camera

    def CapStart(self,instant_camera):
        while True:
            img = np.zeros((1, 1))
            if instant_camera.NumReadyBuffers:
                res = instant_camera.RetrieveResult(1000)
                if res:
                    try:
                        if res.GrabSucceeded():
                            currImg = res.Array
                    finally:
                        res.Release()

    def CalFPS(start_time):
        frametime= start - last_timestamp
        frame_rate = 1 / frametime
        print(frame_rate)

