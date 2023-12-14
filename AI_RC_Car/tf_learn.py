# Copyright Reserved (2020).
# Donghee Lee, Univ. of Seoul
#
__author__ = 'will'

from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
#from sklearn.model_selection import train_test_split

import numpy as np
#import pandas as pd
import tensorflow as tf
#import pickle
from get_image_data import *

class DNN_Driver():
    def __init__(self):
        self.model = keras.models.load_model('./goodmodelp')

    def predict_direction(self, img):
        ret =  self.model.predict(np.array([img]))
        dir = np.argmax(ret)
        print(ret)
        return dir

        
