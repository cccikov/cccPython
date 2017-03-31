list1 = [123]
list2 = [234]
print(list1>list2) # False

list1 = [123,456]
list2 = [234,123]
print(list1>list2) # False

# 数组拼接
list3 = list1 + list2
list4 = list1[:] # 复制数组
list4.extend(list2);
print(list3,list4,list1);
