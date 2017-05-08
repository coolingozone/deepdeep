#  Tensorflow

## Introduction

Tensorflow is the a Open Source framework for Machine Intelligence developed by Google. It using data flow graphs to enable user to easily deploy numberical computation for machine learning. It's flexible architecture allows user  to deploy their computation to multiple CPU or GPU environment whether on desktop, server or mobile device or even embedded system such as Raspberry PI.

You could go to [Tensorflow Site](https://www.tensorflow.org/) to download or learn how to develop with Tensorflow.

Instruction to install Tensorflow on different platforms:

* [Installing TensorFlow on Ubuntu](https://www.tensorflow.org/install/install_linux)
* [Installing TensorFlow on Mac OS X](https://www.tensorflow.org/install/install_mac)
* [Installing TensorFlow on Windows](https://www.tensorflow.org/install/install_windows)
* [Installing TensorFlow from Sources](https://www.tensorflow.org/install/install_sources)  

      $ python

      >>> import tensorflow as tf
      >>> hello =tf.constant('Hello, Tensorflow!')
      >>> sess=tf.Session()
      >>> sess.run(hello)
      'Hello, Tensorflow!'
      >>> a=tf.constant(20)
      >>> b=tf.constant(12)
      >>> a+b
      <tf.Tensor 'add:0' shape=() dtype=int32>
      >>> sess.run(a+b)
      32
      >>> 
This an simple hello world type for tensorflow. What is different from normal python is the present of session command. In Tensorflow when we initialized a variable such as hello with tf.constant("Hello, Tensorflow!‘). the variable is not created at that point. Only when the variable is 'run' by a session such as sess.run(hello) would the variable (constant in this case) would be created.

In the next example, constant a and b are supposed to have value of 10 and 32. However, if we issue command of a+b at this point, the result is nothing. We would need a session to run the addition, sess.run(a+b) and the result would be produced.

## Simple Regress with Tensorflow

Please refer to:
* Jupyter Notebbok [link](http://104.199.205.18:8888/notebooks/DeepWorkshop/SimpleRegression.ipynb) for full explaination.
* Code to download at[link](LinearRegression.py)



