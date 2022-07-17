#直接插入排序
def insertSort(input_list):
    if len(input_list) == 0:
        return []
    sorted_list = input_list
 
    for i in range(1, len(sorted_list)):
        temp = sorted_list[i]
        j = i - 1
        while j >=0 and temp < sorted_list[j]:
            sorted_list[j + 1] = sorted_list[j]
            j -= 1   #与前面元素比较，直到小于0或大于前面元素为止
        sorted_list[j + 1] = temp
    return sorted_list
#折半查找插入排序

def BinarySearch(input_list, end, value):
    left = 0
    right = end - 1
    while left <= right:
        middle = left + (right - left) // 2
        if input_list[middle] > value:
            right = middle - 1
        else:
            left = middle + 1
 
    return left if left < end else -1
 
def BinaryInsertSort(input_list):
    if len(input_list) == 0:
        return []
    result = input_list
    for i in range(1, len(input_list)):
        j = i - 1
        temp = result[i]
        insert_index = BinarySearch(result, i, result[i])
        if insert_index != -1:
            #索引值后移一位
            while j >= insert_index:
                result[j + 1] = result[j]
                j -= 1
            #插入索引值后面
            result[j + 1] = temp
    return result
 
 

if __name__=='__main__':
    intput_list = [49, 38, 65, 87, 76, 13, 27, 49]
    print('排序前:', intput_list)
    sorted_list = BinaryInsertSort(intput_list)
    print('排序后：', sorted_list)
