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


'''匿名函数
python 使用 lambda 来创建匿名函数。
lambda只是一个表达式，函数体比def简单很多。
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
语法
lambda函数的语法只包含一个语句，如下：
lambda [arg1 [,arg2,.....argn]]:expression'''