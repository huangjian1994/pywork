# pywork
标题 Headings：
# 标题 1 (对应HTML中的标签)
## 标题 2 (对应HTML中的标签)
......
###### 标题 6 (对应HTML中的标签)

注意：标题与#之间要留一个空格

段落 Paragraph ：
两段文字之间至少要留有一个空行（one or more blank lines）

字体 Styling Text：
斜体： *This text will be italic*  （对应HTML中的标签）
粗体：**This text will be bold** （对应HTML中的标签）

列表 Lists：
无序号的列表 Unordered Lists
* item
* item
或者
- item
- item
注意： *和-要与列表内容之间要有空格， *是实心的圆点，-是空心的圆点

有序号的列表 Ordered List:s
1. item
2. item
注意： 列表序号与列表内容之间要有空格

嵌套的列表 Nested Lists:
1. item
  1.1 item
  1.2 item
注意： 嵌套列表要缩进2个空格  indenting list items by two spaces

引用 Blockquotes：
引用文字前填加 > （indicate blockquotes with a >）
> 引用文本

代码快 Code Block
To produce a code block in Markdown, simply indent every line of the block by at least 4 spaces or 1 tab.
在每行代码前，使用4个空格或者tab缩进。
例如：
# Title
    if x > y:
        print x

链接 Links：
把链接文字放在中括号[]中，把对应的URL放到小括号()中。（wrapping link text in brackets [ ], and then wrapping the link in parenthesis ( ) ）.
[Sina Blog](blog.sina.com.cn)


##学习导入模块2017年6月22日09:56:45
系统相关的信息模块: import sys
sys.argv 是一个 list,包含所有的命令行参数.    
sys.stdout sys.stdin sys.stderr 分别表示标准输入输出,错误输出的文件对象.    
sys.stdin.readline() 从标准输入读一行 sys.stdout.write("a") 屏幕输出a    
sys.exit(exit_code) 退出程序    
sys.modules 是一个dictionary，表示系统中所有可用的module    
sys.platform 得到运行的操作系统环境    
sys.path 是一个list,指明所有查找module，package的路径.  
操作系统相关的调用和操作: import os
os.environ 一个dictionary 包含环境变量的映射关系   
os.environ["HOME"] 可以得到环境变量HOME的值     
os.chdir(dir) 改变当前目录 os.chdir('d:\\outlook')   
注意windows下用到转义     
os.getcwd() 得到当前目录     
os.getegid() 得到有效组id os.getgid() 得到组id     
os.getuid() 得到用户id os.geteuid() 得到有效用户id     
os.setegid os.setegid() os.seteuid() os.setuid()     
os.getgruops() 得到用户组名称列表     
os.getlogin() 得到用户登录名称     
os.getenv 得到环境变量     
os.putenv 设置环境变量     
os.umask 设置umask     
os.system(cmd) 利用系统调用，运行cmd命令   
内置模块(不用import就可以直接使用)常用内置函数：
help(obj) 在线帮助, obj可是任何类型    
callable(obj) 查看一个obj是不是可以像函数一样调用    
repr(obj) 得到obj的表示字符串，可以利用这个字符串eval重建该对象的一个拷贝    
eval_r(str) 表示合法的python表达式，返回这个表达式    
dir(obj) 查看obj的name space中可见的name    
hasattr(obj,name) 查看一个obj的name space中是否有name    
getattr(obj,name) 得到一个obj的name space中的一个name    
setattr(obj,name,value) 为一个obj的name   
space中的一个name指向vale这个object    
delattr(obj,name) 从obj的name space中删除一个name    
vars(obj) 返回一个object的name space。用dictionary表示    
locals() 返回一个局部name space,用dictionary表示    
globals() 返回一个全局name space,用dictionary表示    
type(obj) 查看一个obj的类型    
isinstance(obj,cls) 查看obj是不是cls的instance    
issubclass(subcls,supcls) 查看subcls是不是supcls的子类  

##################    类型转换  ##################

chr(i) 把一个ASCII数值,变成字符    
ord(i) 把一个字符或者unicode字符,变成ASCII数值    
oct(x) 把整数x变成八进制表示的字符串    
hex(x) 把整数x变成十六进制表示的字符串    
str(obj) 得到obj的字符串描述    
list(seq) 把一个sequence转换成一个list    
tuple(seq) 把一个sequence转换成一个tuple    
dict(),dict(list) 转换成一个dictionary    
int(x) 转换成一个integer    
long(x) 转换成一个long interger    
float(x) 转换成一个浮点数    
complex(x) 转换成复数    
max(...) 求最大值    
min(...) 求最小值  