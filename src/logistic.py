import tensorflow as tf
import numpy as np
import makeTrainingSet
import makeTestingSet


train = makeTrainingSet.TrainingSet()
train.readImageList()
trainX = train.trX()
trainY = train.trY()

test = makeTestingSet.TestingSet()
test.readImageList()
testX = test.teX()
testY = test.teY()

tex = np.zeros((test.numOfFile, 40000))
trx = np.zeros((train.numOfFile, 40000))


for k in range(0, train.numOfFile):
    for i in range(0,200):
        for j in range(0,200):
            trx[k, i*200+j] = trainX[k][i][j][0]

for k in range(0, test.numOfFile):
    for i in range(0,200):
        for j in range(0,200):
            tex[k, i*200+j] = testX[k][i][j][0]



x = tf.placeholder(tf.float32, [None, 40000])
y = tf.placeholder(tf.float32, [None, 2])

W = tf.Variable(tf.zeros([40000, 2]))
b = tf.Variable(tf.zeros([2]))

hypothesis = tf.add(tf.matmul(x, W),b)
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(hypothesis, y))

optimizer = tf.train.AdamOptimizer(learning_rate=0.001).minimize(cost)

init = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init)

for i in range(50):
    print np.shape(trx), np.shape(trainY)
    sess.run(optimizer, feed_dict={x: trx, y: trainY})
    print i, sess.run(cost, feed_dict={x: trx, y: trainY})

correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(hypothesis,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print(sess.run(accuracy, feed_dict={x: tex, y: testY}))