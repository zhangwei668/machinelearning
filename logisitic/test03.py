#从疝气病症状预测病马的死亡率(梯度上升)
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
函数说明:梯度上升算法
 
Parameters:
    dataMatIn - 数据集
    classLabels - 数据标签
Returns:
    weights.getA() - 求得的权重数组(最优参数)
"""
def gradAscent(dataMatIn, classLabels):
    dataMatrix = np.mat(dataMatIn)                                        #转换成numpy的mat
    labelMat = np.mat(classLabels).transpose()                            #转换成numpy的mat,并进行转置
    m, n = np.shape(dataMatrix)                                            #返回dataMatrix的大小。m为行数,n为列数。
    alpha = 0.01                                                        #移动步长,也就是学习速率,控制更新的幅度。
    maxCycles = 500                                                        #最大迭代次数
    weights = np.ones((n,1))
    for k in range(maxCycles):
        h = sigmoid(dataMatrix * weights)                                #梯度上升矢量化公式
        error = labelMat - h
        weights = weights + alpha * dataMatrix.transpose() * error
    return weights.getA()                                                #将矩阵转换为数组，并返回
 
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
    trainWeights = gradAscent(np.array(trainingset), trainingLabels)
    #print(trainWeights)
    errorCount = 0; numTestVec = 0.0
    for line in frTest.readlines():
        numTestVec += 1.0
        currLines = line.strip().split('\t')
        LineArr = []
        for i in range(len(currLines)-1):
            LineArr.append(float(currLines[i]))
        
        if int(classifyVector(np.array(LineArr), trainWeights[:,0])) != int(currLines[-1]):
           errorCount += 1
    errorRate = (float(errorCount)/numTestVec) * 100
    print("测试集错误率为：%.2f%%" % errorRate)

 
if __name__ == '__main__':
    colicTest()

 

