from sklearn.linear_model import LogisticRegression
 
"""
函数说明:使用Sklearn构建Logistic回归分类器
"""
def colicSklearn():
    frTrain = open('F:\machinelearning\logisitic\horseColicTraining.txt')
    frTest = open('F:\machinelearning\logisitic\horseColicTest.txt')                                             #打开测试集
    trainingSet = []; trainingLabels = []
    testSet = []; testLabels = []
    for line in frTrain.readlines():
        currLine = line.strip().split('\t')
        lineArr = []
        for i in range(len(currLine)-1):
            lineArr.append(float(currLine[i]))
        trainingSet.append(lineArr)
        trainingLabels.append(float(currLine[-1]))
    for line in frTest.readlines():
        currLine = line.strip().split('\t')
        lineArr =[]
        for i in range(len(currLine)-1):
            lineArr.append(float(currLine[i]))
        testSet.append(lineArr)
        testLabels.append(float(currLine[-1]))
    #求解方法和求解器收敛的最大迭代次数。（sag，saga适合大数据，liblinear适合小数据）
    classifier = LogisticRegression(solver='liblinear',max_iter=10).fit(trainingSet, trainingLabels)
    test_accurcy = classifier.score(testSet, testLabels) * 100
    print('正确率:%f%%' % test_accurcy)
 
if __name__ == '__main__':
    colicSklearn()