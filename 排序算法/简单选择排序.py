def selectsort(input_list):

    if len(input_list) == 0:
        return
    sorted_list = input_list
    lenth = len(sorted_list)
    for i in range(lenth):
        min_dex = i
        for j in range(i+1, lenth):
            if sorted_list[min_dex] > sorted_list[j]:
                min_dex = j
        if min_dex == i:
            continue
        temp = sorted_list[i]
        sorted_list[i] = sorted_list[min_dex]
        sorted_list[min_dex] = temp
    return sorted_list

if __name__=='__main__':
    input_list = [6,4,8,9,2,3,1]
    print('排序前：',input_list)
    sorted_list = selectsort(input_list)
    print('排序后：',sorted_list)
            