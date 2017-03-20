# 数据类型

# 整型
theInt = 100

# 浮点型
thefloat = 3.14

# 字符串
theStr = "hello"
theLongStr = """氨基酸的绿卡介绍的
阿萨德垃圾数量单价
按实际达拉斯就看到
"""

# 布尔值
theBool = False

# 空值
theNull = None;

print(theInt,thefloat,theStr,theLongStr,theBool,theNull);

# 常量 通常用大写
PI = 3.1415 # 只是一种约定俗成,没人说不可以修改

print(10/3,10//3,10%3)# 3.3333333333333335 3 1


toInt = int("123456");# 转化为整型
toStr = str(123123);# 转化为字符串
toFloat = float(12);# 转化为浮点数
print(toInt,toStr,toFloat);# 123456 123123 12.0

theType1 = type(toInt);
theType2 = type(toStr);
theType3 = type(toFloat);
theType4 = type(theNull);
print(theType1,theType2,theType3,theType4) # <class 'int'> <class 'str'> <class 'float'> <class 'NoneType'>
