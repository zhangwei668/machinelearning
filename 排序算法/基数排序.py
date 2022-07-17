import random
def radix_sort(input_list):
    max_num = max(input_list)
    place = 1
    while max_num >= 10**place:
        place += 1
    for i in range(place):
        buckets = [[] for _ in range(10)]  # _表示在不在意变量的值，只是用于循环迭代，生成10个空列表，
        for num in input_list:
            radix = int(num/(10**i) % 10)
            buckets[radix].append(num)
        j = 0
        for k in range(10):
            for num in buckets[k]:
                input_list[j] = num
                j += 1
    return input_list

if __name__ == '__main__':
    #input_list = [random.randint(1, 99) for i in range(10)]  # 制造10个数据
    input_list = [25, 13, 33, 17, 22, 96, 32, 15, 9, 25, 55, 18]
    print(radix_sort(input_list))



    
