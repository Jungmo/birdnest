import os
import GlobalVariable
import cv2
import numpy as np

class TrainingSet:
    imageList = os.listdir(GlobalVariable.trainingSetPath)
    listPath = os.path.join(GlobalVariable.trainingSetPath, "list.txt")
    lablePath = os.path.join(GlobalVariable.trainingSetPath, "label.txt")
    imagePath = []

    def __init__(self):
        pass

    def readImageList(self):
        f = open(self.listPath, 'r')
        while True:
            line = f.read().splitlines()
            if not line: break
            self.imagePath.append(line)

    def trX(self):
        ret = []
        for i in range(0 , len(self.imagePath[0])):
            path = os.path.join(GlobalVariable.trainingSetPath ,self.imagePath[0][i])
            image = cv2.imread(path, 1)
            image = np.array(image)
            ret.append(image)
        return ret

    def trY(self):
        f = open(self.labelpath,'r')
