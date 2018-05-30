# /usr/bin/env python
# -*- coding: UTF-8 -*-
import os

# str1 = input("请输入：")
# print("你输入的内容是: ", str1)

f = open("foo.txt", 'w')
f.write('Hello, world!123')
f.close()
# 读取文件
f1 = open("foo.txt", "r+")
len1 = f1.read(20)
print("读取的为： ", len1)

position = f1.tell()
print("当前位置：", position)
# 把指针重新定位到文件开头
f1.seek(0, 0)
str1 = f1.read(5)
print("重新读取字符串：", str1)
f1.close()

# 重命名文件

# os.renames("foo.txt", "foo1.txt")
# 删除文件
# remove()
# 获取当前工作目录
print(os.getcwd())

