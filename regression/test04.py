#预测鲍鱼年龄，根据数据集拟合局部加权线性回归
#局部加权线性回归
from matplotlib.font_manager import FontProperties
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
def lwlr(testPoint, xArr, yArr, k = 1.0):
    """
    函数说明:使用局部加权线性回归计算回归系数w
    Parameters:
        testPoint - 测试样本点
        xArr - x数据集
        yArr - y数据集
        k - 高斯核的k,自定义参数
    Returns:
        ws - 回归系数
    """ 
    xMat = np.mat(xArr); yMat = np.mat(yArr).T
    m = np.shape(xMat)[0]
    weights = np.mat(np.eye((m)))                                        #创建权重对角矩阵
    for j in range(m):                                                  #遍历数据集计算每个样本的权重
        diffMat = testPoint - xMat[j, :]                                 
        weights[j, j] = np.exp(diffMat * diffMat.T/(-2.0 * k**2))
    xTx = xMat.T * (weights * xMat)                                        
    if np.linalg.det(xTx) == 0.0:
        print("矩阵为奇异矩阵,不能求逆")
        return
    ws = xTx.I * (xMat.T * (weights * yMat))                            #计算回归系数
    return testPoint * ws
def lwlrTest(testArr, xArr, yArr, k=1.0):  
    """
    函数说明:局部加权线性回归测试
    Parameters:
        testArr - 测试数据集
        xArr - x数据集
        yArr - y数据集
        k - 高斯核的k,自定义参数
    Returns:
        ws - 回归系数
    """
    m = np.shape(testArr)[0]                                            #计算测试数据集大小
    yHat = np.zeros(m)    
    for i in range(m):                                                    #对每个样本点进行预测
        yHat[i] = lwlr(testArr[i],xArr,yArr,k)
    return yHat
def standRegres(testArr, xArr,yArr):
    """
    函数说明:计算回归系数w并预测y
    Parameters:
        xArr - x数据集
        yArr - y数据集
    Returns:
        ws - 回归系数
    """
    xMat = np.mat(xArr); yMat = np.mat(yArr).T
    xTx = xMat.T * xMat                            #根据文中推导的公示计算回归系数
    if np.linalg.det(xTx) == 0.0:
        print("矩阵为奇异矩阵,不能求逆")
        return
    ws = xTx.I * (xMat.T*yMat)
    return np.mat(testArr) * ws
def rssError(yArr, yHatArr):
    """
    误差大小评价函数
    Parameters:
        yArr - 真实数据
        yHatArr - 预测数据
    Returns:
        误差大小
    """
    return ((yArr - yHatArr) **2).sum()   
def diffK_error():
    abX, abY = loadDataSet('F:\machinelearning\\regression\\abalone.txt')
    print('训练集与测试集相同：局部加权线性回归，不同核k对预测的影响：')
    yHat1 = lwlrTest(abX[0:99], abX[0:99], abY[0:99], 0.1)
    yHat2 = lwlrTest(abX[0:99], abX[0:99], abY[0:99], 1.0)
    yHat3 = lwlrTest(abX[0:99], abX[0:99], abY[0:99], 10)
    print('k=0.1时，误差为：', rssError(abY[0:99], yHat1.T))
    print('k=1.0时，误差为：', rssError(abY[0:99], yHat2.T))
    print('k=10时，误差为：', rssError(abY[0:99], yHat3.T))
    print('')
    print('训练集与测试集不同：局部加权线性回归，k过小可能导致过拟合，核k对预测的影响如下：')
    yHat1 = lwlrTest(abX[100:199], abX[0:99], abY[0:99], 0.1)
    yHat2 = lwlrTest(abX[100:199], abX[0:99], abY[0:99], 1.0)
    yHat3 = lwlrTest(abX[100:199], abX[0:99], abY[0:99], 10)
    print('k=0.1时，误差为：', rssError(abY[100:199], yHat1.T))
    print('k=1.0时，误差为：', rssError(abY[100:199], yHat2.T))
    print('k=10时，误差为：', rssError(abY[100:199], yHat3.T))
    print('')
    print('训练集与测试集不同:简单的线性归回与k=1时的局部加权线性回归对比:')
    yHat = standRegres(abX[100:199], abX[0:99], abY[0:99])
    print('简单的线性回归误差大小:', rssError(abY[100:199], yHat.T.A))
    print('k=1时,误差大小为:', rssError(abY[100:199], yHat2.T))

if __name__ == '__main__':
    diffK_error()
