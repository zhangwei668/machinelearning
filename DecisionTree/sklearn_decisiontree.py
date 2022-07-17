from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn import tree
import pandas as pd
import numpy as np
import pydotplus    
from io import StringIO
import graphviz 


if __name__ == '__main__':
    with open('F:\machinelearning\DecisionTree\lenses.txt', 'r') as fr:                                        #加载文件
        lenses = [inst.strip().split('\t') for inst in fr.readlines()]        #处理文件
    lenses_target = []                                                        #提取每组数据的类别，保存在列表里
    for each in lenses:
        lenses_target.append(each[-1])
 
    lensesLabels = ['age', 'prescript', 'astigmatic', 'tearRate']            #特征标签       
    lenses_list = []                                                        #保存lenses数据的临时列表
    lenses_dict = {}                                                        #保存lenses数据的字典，用于生成pandas
    for each_label in lensesLabels:                                            #提取信息，生成字典
        for each in lenses:
            lenses_list.append(each[lensesLabels.index(each_label)])
        lenses_dict[each_label] = lenses_list
        lenses_list = []
    #print(lenses_dict)                                                        #打印字典信息
    lenses_pd = pd.DataFrame(lenses_dict)                                    #生成pandas.DataFrame
    #print(lenses_pd)
    le = LabelEncoder()
    #columns属性以返回给定 pd.DataFrame 的列标签lensesLables
    for col in lenses_pd.columns:
        #拟合标签编码器并返回编码标签
        lenses_pd[col] = le.fit_transform(lenses_pd[col])
    #print(lenses_pd)

    clf = tree.DecisionTreeClassifier(max_depth = 4)                        #创建DecisionTreeClassifier()类
    clf = clf.fit(lenses_pd.values.tolist(), lenses_target)                    #使用数据，构建决策树
     
    dot_data = tree.export_graphviz(clf, out_file = None,                            #绘制决策树
                        feature_names = lenses_pd.keys(),
                        class_names = lenses_target,
                        filled=True, rounded=True,
                        special_characters=True)
    graph = graphviz.Source(dot_data)
    graph.view()  
                                                  #保存绘制好的决策树，以PDF的形式存储。