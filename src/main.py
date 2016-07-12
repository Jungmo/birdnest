import tensorflow as tf
import makeTrainingSet

a = makeTrainingSet.TrainingSet()

a.readImageList()
trainX = a.trX()
trainY = a.trY()
