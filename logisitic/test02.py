#从疝气病症状预测病马的死亡率(随机梯度)
import numpy as np
import random

"""
函数说明:sigmoid函数
Parameters:
    inX - 数据
Returns:
    sigmoid函数
"""
def sigmoid(inX):
    return 1.0 / (1 + np.exp(-inX))
"""
函数说明:分类函数
Parameters:
    inX - 特征向量
    weights - 回归系数
Returns:
    分类结果
"""
def classifyVector(inX, weights):
    prob = sigmoid(sum(inX*weights))
    if prob > 0.5: 
        return 1.0
    else: return 0.0

"""
函数说明:改进的随机梯度上升算法
Parameters:
    dataMatrix - 数据数组
    classLabels - 数据标签
    numIter - 迭代次数
Returns:
    weights - 求得的回归系数数组(最优参数)
"""
def stocGraAsent1(dataMatrix, classLabels, numIter=150):
    m,n = np.shape(dataMatrix)
    weights = np.ones(n)
    for j in range(numIter):
        dataIndex = list(range(m))
        for i in range(m):
            alpha = 4/(1.0+j+i)+0.01
            randIndex = int(random.uniform(0,len(dataIndex)))
            h = sigmoid(sum(dataMatrix[dataIndex[randIndex]]*weights))
            error = classLabels[dataIndex[randIndex]] - h
            weights = weights + alpha * error * dataMatrix[dataIndex[randIndex]]
            del(dataIndex[randIndex])
    return weights
"""
函数说明:使用Python写的Logistic分类器做预测
"""
def colicTest():
    frTrain = open('F:\machinelearning\logisitic\horseColicTraining.txt')
    frTest = open('F:\machinelearning\logisitic\horseColicTest.txt')
    trainingset = []; trainingLabels =[]
    for line in frTrain.readlines():
        currLines = line.strip().split('\t')
        LineArr = []
        #去除最后一列标签
        for i in range(len(currLines)-1):
            LineArr.append(float(currLines[-1]))
        trainingset.append(LineArr)
        trainingLabels.append(float(currLines[-1]))
    trainWeights = stocGraAsent1(np.array(trainingset), trainingLabels, 500)
    errorCount = 0; numTestVec = 0.0
    for line in frTest.readlines():
        numTestVec += 1.0
        currLines = line.strip().split('\t')
        LineArr = []
        for i in range(len(currLines)-1):
            LineArr.append(float(currLines[i]))
        if int(classifyVector(np.array(LineArr), trainWeights)) != int(currLines[-1]):
           errorCount += 1
    errorRate = (float(errorCount)/numTestVec) * 100
    print("测试集错误率为：%.2f%%" % errorRate)

 
if __name__ == '__main__':
    colicTest()

 

