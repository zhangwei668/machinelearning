#利用梯度上升求w
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import numpy as np
import random
#梯度上升算法
def loadDataSet(fileName):
    dataMat = []
    labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([float(lineArr[0]), float(lineArr[1])])
        labelMat.append(float(lineArr[2]))
    fr.close()
    return dataMat, labelMat
"""
函数说明:绘制数据集

"""
def plotDataSet():
    dataMat, labelMat = loadDataSet('F:\machinelearning\\regression\\ex0.txt')                                    #加载数据集
    dataArr = np.array(dataMat)                                            #转换成numpy的array数组
    n = np.shape(dataMat)[0]                                            #数据个数
    xcord1 = []; ycord1 = []                                            #正样本

    for i in range(n):                                                    #根据数据集标签进行分类
            xcord1.append(dataArr[i,1]); ycord1.append(labelMat[i])
    fig = plt.figure()
    ax = fig.add_subplot(111)                                            #添加subplot
    ax.scatter(xcord1, ycord1, s = 20, c = 'blue',alpha=.5)

    plt.title('DataSet')                                                #绘制title
    plt.xlabel('x'); plt.ylabel('y')                                    #绘制label
    plt.show()

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
    alpha = 0.001                                                        #移动步长,也就是学习速率,控制更新的幅度。
    maxCycles = 500                                                       #最大迭代次数
    weights = np.ones((n,1))
    weights_array = np.array([])
    for k in range(maxCycles):
        h = (dataMatrix * weights)                                #梯度上升矢量化公式
        error = h - labelMat
        weights = weights - alpha * dataMatrix.transpose() * error
    return weights                                        #将矩阵转换为数组，返回权重数组
#随机梯度算法
def stocGradAscent1(dataMatrix, classLabels, numIter=150):
    m,n = np.shape(dataMatrix)                                                #返回dataMatrix的大小。m为行数,n为列数。
    weights = np.ones(n)                                                       #参数初始化
    weights_array = np.array([])                                            #存储每次更新的回归系数
    for j in range(numIter):                                           
        dataIndex = list(range(m))
        for i in range(m):           
            alpha = 4/(1.0+j+i)+0.01                                            #降低alpha的大小，每次减小1/(j+i)。
            randIndex = int(random.uniform(0,len(dataIndex)))                #随机选取样本
            h = (sum(dataMatrix[dataIndex[randIndex]]*weights))          #选择随机选取的一个样本，计算h
            error = h - classLabels[dataIndex[randIndex]]                          #计算误差
            #可以去除1/m 试试结果，可能效果更好，等于α加大，把α与1/m看成一个整体去调整
            weights = weights - alpha * error * dataMatrix[dataIndex[randIndex]]   #更新回归系数
            weights_array = np.append(weights_array,weights,axis=0)         #添加回归系数到数组中
            del(dataIndex[randIndex])                                         #删除已经使用的样本
    weights_array = weights_array.reshape(numIter*m,n)                         #改变维度
    return weights                                            #返回
 
#绘制决策边界
def plotBestFit(weights):
    dataMat, labelMat = loadDataSet('F:\machinelearning\\regression\\ex0.txt')                                    #加载数据集
    dataArr = np.array(dataMat)                                            #转换成numpy的array数组
    n = np.shape(dataMat)[0]                                            #数据个数
    xcord1 = []; ycord1 = []                                            #正样本

    for i in range(n):                                                    #根据数据集标签进行分类
            xcord1.append(dataArr[i,1]); ycord1.append(labelMat[i])
    fig = plt.figure()
    ax = fig.add_subplot(111)                                            #添加subplot
    ax.scatter(xcord1, ycord1, s = 20, c = 'blue',alpha=.5)

    x = np.arange(0.0, 1.0, 0.01)
    #令z=0，求x2 关于x1的函数
    y = (float(weights[0]) + float(weights[1]) * x) 
    plt.plot(x, y)
    plt.title('DataSetfit')                                                #绘制title
    plt.xlabel('x'); plt.ylabel('y')                                    #绘制label
    plt.show()



if __name__ == '__main__':
    dataMat, labelMat = loadDataSet('F:\machinelearning\\regression\\ex0.txt')  
    #plotDataSet()

    #梯度上升     
    weights = gradAscent(dataMat, labelMat)
    print(weights)
    plotBestFit(weights)
    """
    #随机梯度上升
    weights = stocGradAscent1(np.array(dataMat),labelMat)
    print(weights)
    plotBestFit(weights)
    """
    