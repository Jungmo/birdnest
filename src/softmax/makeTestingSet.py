import os
import GlobalVariable
import cv2
import numpy as np

class TestingSet:
    imageList = os.listdir(GlobalVariable.testSetPath)
    listPath = os.path.join(GlobalVariable.testSetPath, "list.txt")
    labelPath = os.path.join(GlobalVariable.testSetPath, "label.txt")
    imagePath = []
    numOfFile = 0

    def __init__(self):
        pass

    def readImageList(self):
        f = open(self.listPath, 'r')
        while True:
            line = f.read().splitlines()
            if not line: break
            self.imagePath.append(line)
        self.numOfFile = len(self.imagePath[0])

    def teX(self):
        temp = []
        for i in range(0 , self.numOfFile):
            path = os.path.join(GlobalVariable.testSetPath, self.imagePath[0][i])
            image = cv2.imread(path, 1)
            temp.append(image)
            ret = np.array(temp)
        return ret

    def teY(self):
        f = open(self.labelPath,'r')
        ret = []
        for i in range(0, self.numOfFile):
            line = f.readline()
            if 1 == int(line):
                ret.append([1,0])
            elif 2 == int(line):
                ret.append([0,1])
        return ret