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

class digit_data(object):
    def __init__(self):
        self.train = train_test()
        self.test = train_test()

    def input_data(self):
        mnist = input_data.read_data_sets("MNIST_data", one_hot=True)
        images = np.r_[mnist.train.images, mnist.test.images]
        labels = np.r_[mnist.train.labels, mnist.test.labels]
        zeros = np.zeros((labels.shape[0], 6))
        labels = np.c_[labels, zeros]
        print("Loading the operators' datasets....")
        op_images, op_labels = get_images_labels()
        images, labels = np.r_[images, op_images], np.r_[labels, op_labels]
        print("Generating the train_data and test_data....")
        sss = StratifiedShuffleSplit(n_splits=16, test_size=0.15, random_state=23)
        for train_index, test_index in sss.split(images, labels):
            self.train.images, self.test.images = images[train_index], images[test_index]
            self.train.labels, self.test.labels = labels[train_index], labels[test_index]

