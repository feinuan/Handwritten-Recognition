import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
from image_processing import *
from sklearn.model_selection import StratifiedShuffleSplit
import os
from tqdm import tqdm

SYMBOL = {0: '0',
          1: '1',
          2: '2',
          3: '3',
          4: '4',
          5: '5',
          6: '6',
          7: '7',
          8: '8',
          9: '9',
          10:'+',
          11:'-',
          12:'*',
          13:'/',
          14:'(',
          15:')'}

class train_test(object):
    def __init__(self):
        self.images = None
        self.labels = None
        self.offset = 0

    def next_batch(self, batch_size):
        if self.offset + batch_size <= self.images.shape[0]:
            batch_images = self.images[self.offset:self.offset + batch_size]
            batch_labels = self.labels[self.offset:self.offset + batch_size]
            self.offset = (self.offset + batch_size) % self.images.shape[0]
        else:
            new_offset = self.offset + batch_size - self.images.shape[0]
            batch_images = self.images[self.offset:-1]
            batch_labels = self.labels[self.offset:-1]
            batch_images = np.r_[batch_images, self.images[0:new_offset]]
            batch_labels = np.r_[batch_labels, self.labels[0:new_offset]]
            self.offset = new_offset
        return batch_images, batch_labels