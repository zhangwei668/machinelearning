"""
Merge_Sort 归并排序
"""
# 切割数组 的函数
def merge_sort(input_list):
 # 如果长度小于等于1 ，不能再分割了
 if len(input_list) <= 1:
  return input_list
 
 # 根据列表长度确定拆分的中间位置
 mid_index = len(input_list)//2
 
 # 使用切片实现对列表的切分
 # left_list = input_list[:mid_index]
 # right_list = input_list[mid_index:]
 
 # 递归调用，无限切割下去,left执行到最后，最后一层left数组只有一个元素，接下去执行right，然后合并排序，
 # 然后返回上一层继续执行上一层right，分左右合并，然后返回上一层合并left，right，如此到顶层。
 left_list = merge_sort(input_list[:mid_index])
 right_list = merge_sort(input_list[mid_index:])
 return merge(left_list, right_list)
 
# 排序的函数
def merge(left_list, right_list):
 l_index,r_index = 0,0
 merge_list = []
 # 判断列表里面是否还有元素可以用
 while l_index < len(left_list) and r_index < len(right_list):
  # 哪边的元素小于另外一边的的元素就把哪边的元素加入进去，对应的索引加一
  if left_list[l_index] < right_list[r_index]:
   merge_list.append(left_list[l_index])
   l_index += 1
  else:
   merge_list.append(right_list[r_index])
   r_index += 1
 # 下面的这两个就是，如果有一个列表全部添加了，另外一个列表直接添加到merge_list里面了
 merge_list += left_list[l_index:]
 merge_list += right_list[r_index:]
 return merge_list
 
if __name__ == '__main__':
 input_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
 print(f'原列表的顺序：{input_list}')
 input_list = merge_sort(input_list)
 print(f'选择排序之后的列表的顺序：{input_list}')
