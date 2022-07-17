#利用最小二乘法求w
import matplotlib.pyplot as plt
import numpy as np
 
def loadDataSet(fileName):
    """
    函数说明:加载数据
    Parameters:
        fileName - 文件名
    Returns:
        xArr - x数据集
        yArr - y数据集
    """
    numFeat = len(open(fileName).readline().split('\t')) - 1
    xArr = []; yArr = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr =[]
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        xArr.append(lineArr)
        yArr.append(float(curLine[-1]))
    return xArr, yArr
 
def standRegres(xArr,yArr):
    """
    函数说明:计算回归系数w
    Parameters:
        xArr - x数据集
        yArr - y数据集
    Returns:
        weights - 回归系数
    """
    #一、np.linalg.det():矩阵求行列式
    #二、np.linalg.inv()：矩阵求逆
    #三、np.linalg.norm():求范数
    xMat = np.mat(xArr); yMat = np.mat(yArr).T
    xTx = xMat.T * xMat                            #根据文中推导的公示计算回归系数
    if np.linalg.det(xTx) == 0.0:
        print("矩阵为奇异矩阵,不能求逆")
        return
    weights = xTx.I * (xMat.T*yMat)
    return weights
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
def fitrate():
    xArr, yArr = loadDataSet('F:\machinelearning\\regression\ex0.txt')       #加载数据集
    weights = standRegres(xArr, yArr)                                        #计算回归系数
    xMat = np.mat(xArr)                                                    #创建xMat矩阵
    yMat = np.mat(yArr)                                                    #创建yMat矩阵
    yHat = xMat * weights
    #输出矩阵r的意义：r00，r11为yhat，ymat自身拟合度为1，r01，r10为两者拟合度。
    print(np.corrcoef(yHat.T, yMat))
if __name__ == '__main__':
    xArr, yArr = loadDataSet('F:\machinelearning\\regression\ex0.txt')
    weights = standRegres(xArr,yArr)
    print(weights)
    plotBestFit(weights)
    #预测拟合度
    #fitrate()