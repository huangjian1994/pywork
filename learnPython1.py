# 定义函数
def printme(str):
    print(str)
    return;


# 调用函数
printme("我要自己打印的")


# 传可变对象
def changeme(myList):
    "修改传入的列表"
    myList.append([1, 22, 23, 24]);
    print("函数内取值：", myList);
    return


# 调用changeme函数
myList = [5, 55, 555];
changeme(myList);
print("函数外取值：", myList)

'''不定长参数
 你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，
 和上述2种参数不同，声明时不会命名。基本语法如下：'''


# 可写函数声明
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出：")
    print(arg1)
    for var in vartuple:
        print(var)
        return;


# 调用printinfo
printinfo(10)
printinfo(270, 60, 70);


