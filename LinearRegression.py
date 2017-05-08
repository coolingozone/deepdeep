import tensorflow as tf

import numpy as np
#import matplotlib.pyplot as plt

# 0 is the mean of the normal distribution you are choosing from
# 1.6 is the standard deviation of the normal distribution
# 100 is the number of elements you get in array noise

np.random.seed(seed=234)
noise = np.random.normal(0,1.2,100)
#generating the training data
train_X=np.asarray(np.arange(0,100,1))
train_Y=0.2*train_X+0.6+noise
#plt.scatter(train_x,traing_y)
#plt.show()
n_samples = train_X.shape[0]

# Parameters
learning_rate = 0.01
training_epochs = 1000
display_step = 50

# tf Graph Input
X = tf.placeholder("float")
Y = tf.placeholder("float")

# Set model weights
W = tf.Variable(np.random.randn(), name="weight")
b = tf.Variable(np.random.randn(), name="bias")

# Construct a linear model
pred = tf.add(tf.multiply(X, W), b)

loss = tf.reduce_mean(tf.pow(pred - Y, 2)) / (2 * n_samples)
# Gradient descent
# Gradient descent
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)
# Initializing the variables
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    # Fit all training data
    for epoch in range(training_epochs):
        for (x, y) in zip(train_X, train_Y):
            sess.run(optimizer, feed_dict={X: x, Y: y})

        # Display logs per epoch step
        if (epoch + 1) % display_step == 0:
            c = sess.run(loss, feed_dict={X: train_X, Y: train_Y})
            print "Epoch:", '%04d' % (epoch + 1), "loss=", "{:.9f}".format(c), \
                "W=", sess.run(W), "b=", sess.run(b)
        ww = sess.run(W)
        bb = sess.run(b)


#plt.scatter(train_x,traing_y,color='green',label='Train Data')
#pred_y=train_X*ww+bb
#plt.plot(train_X,pred_y,color='red',label='Fitted Line')
# Place a legend to the right of this smaller subplot.
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#plt.show()
