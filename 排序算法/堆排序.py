def heap_sort(input_list):
    first = len(input_list) // 2 - 1
    for start in range(first, -1, -1):
        # 从下到上，从右到左对每个非叶节点进行调整，循环构建成大顶堆
        big_heap(input_list, start, len(input_list) - 1)
    for end in range(len(input_list) - 1, 0, -1):
        # 交换堆顶和堆尾的数据
        input_list[0], input_list[end] = input_list[end], input_list[0]
        # 重新调整完全二叉树，构造成大顶堆
        big_heap(input_list, 0, end - 1)
    return input_list
  
  
def big_heap(input_list, start, end):
    root = start
    # 左孩子的索引
    child = root * 2 + 1
    while child <= end:
        # 节点有右子节点，并且右子节点的值大于左子节点，则将child变为右子节点的索引
        if child + 1 <= end and input_list[child] < input_list[child + 1]:
            child += 1
        if input_list[root] < input_list[child]:
            # 交换节点与子节点中较大者的值
            input_list[root], input_list[child] = input_list[child], input_list[root]
            # 交换值后，如果存在孙节点，则将root设置为子节点，继续与孙节点进行比较
            root = child
            child = root * 2 + 1
        else:
            break
  
  
if __name__ == '__main__':
    input_list = [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]
    print(heap_sort(input_list))