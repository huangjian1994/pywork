# /usr/bin/env python
# -*- coding: UTF-8 -*-



str1 = input("请输入：")
print("你输入的内容是: ", str1)

# 打开一个文件
fo = open("foo.txt", "wb")
print( "文件名: ", fo.name)
print ("是否已关闭 : ", fo.closed)
print ("访问模式 : ", fo.mode)
# print ("末尾是否强制加空格 : ", fo.softspace )