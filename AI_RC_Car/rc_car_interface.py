# Copyright(c) Reserved 2020.
# Donghee Lee, University of Soul
#
__author__ = 'will'

import numpy as np
import cv2
import serial
#from picamera.array import PiRGBArray
#from picamera import PiCamera
from picamera2 import Picamera2, Preview
from pyzbar.pyzbar import decode
import time

class RC_Car_Interface():

    def __init__(self):
        self.left_wheel = 0
        self.right_wheel = 0
        self.camera = Picamera2()
        self.camera.resolution = (500,990)         # set camera resolution to (320, 320)
        #self.camera.resolution = (1000,1980)         # set camera resolution to (320, 320)

        self.camera.color_effects = (128,128)      # set camera to black and white
        self.prev = 0
        #self.camera.start_preview(Preview.QTGL)
        self.camera.start()
        self.ser = serial.Serial('/dev/serial/by-id/usb-Arduino_Srl_Arduino_Uno_7543134333435161B042-if00',9600)
        self.qr = False

    def finish_iteration(self):
        print('finish iteration')
        
    def stop(self):
        cmd = ("P\n").encode('ascii')
        #print("My cmd is %s" % cmd)
        self.ser.write(cmd)
        #   For debugging, read cmd from arduino and print it    
        #read_serial=self.ser.readline()
        #print (read_serial)

    def set_direction(self, dir):
        if dir == 0:    # 0
            self.prev = 0;
            cmd = ("S\n").encode('ascii')
            #print("My cmd is %s" % cmd)
            self.ser.write(cmd)
        #   For debugging, read cmd from arduino and print it    
            #read_serial=self.ser.readline()
            #print (read_serial)
            cmd = ("P\n").encode('ascii')
            self.ser.write(cmd)
        elif dir == 1:  # 1
            self.prev = 1;
            cmd = ("R\n").encode('ascii')
            #print("My cmd is %s" % cmd)
            self.ser.write(cmd)
        #   For debugging, read cmd from arduino and print it    
            #read_serial=self.ser.readline()
            #print (read_serial)
            cmd = ("P\n").encode('ascii')
            self.ser.write(cmd)
        elif dir == 2:   # 2
            self.set_direction(self.prev)
            #print("no line")
            cmd = ("P\n").encode('ascii')
            self.ser.write(cmd)
        elif dir == 3:   # -1
            self.prev = 3;
            cmd = ("L\n").encode('ascii')
            #print("My cmd is %s" % cmd)
            self.ser.write(cmd)
        #   For debugging, read cmd from arduino and print it    
            #read_serial=self.ser.readline()
            #print (read_serial)
            cmd = ("P\n").encode('ascii')
            self.ser.write(cmd)


        
    def get_image_from_camera(self):
        
        time.sleep(1)
        img = self.camera.capture_array("main")
        #print("capture!!")
        
        
        for code in decode(img):
                qr = code.data.decode('utf-8')
                print("!!! QR CODE DETECTED:: ", qr)
                print(">>> SLEEP ...")
                
                cmd = ("Q\n").encode('ascii')
                self.ser.write(cmd)
                self.qr = True
                

        
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img2 = cv2.resize(img2,(64,64))
        

        return img2

# Test Only
# RC_Car_Interface().get_image_from_camera()
