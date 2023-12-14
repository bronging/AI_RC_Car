# Copyright Reserved (2020).
# Donghee Lee, Univ. of Seoul
#
__author__ = 'will'

from rc_car_interface import RC_Car_Interface
from tf_learn import DNN_Driver
import numpy as np
from tensorflow import keras
import time
import cv2



class SelfDriving:

    def __init__(self):
        self.rc_car_cntl = RC_Car_Interface()
        self.dnn_driver = DNN_Driver()
        

    def drive(self):
        while True:


            img = self.rc_car_cntl.get_image_from_camera()

            direction = self.dnn_driver.predict_direction(img)         # predict with single image
            print(direction)
            self.rc_car_cntl.set_direction(direction)


            #self.rc_car_cntl.stop()
            
            #time.sleep(1)
            
        cv2.destroyAllWindows()

SelfDriving().drive()
