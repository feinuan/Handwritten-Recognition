import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
#标准差为0.1的正态分布
def weight_variable(shape):
    initial = tf.truncated_normal(shape,stddev=0.1)
    return tf.Variable(initial)

#0.1的偏差常数，为了避免死亡节点
def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)
#二维卷积函数
#strides代表卷积模板移动的步长，全是1代表走过所有的值
#padding设为SAME意思是保持输入输出的大小一样，使用全0补充
def conv2d(x,W):
    return tf.nn.conv2d(x,W,str