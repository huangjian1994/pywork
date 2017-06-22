#猜数字
import random
s = int(random.uniform(1,100))
print(s)
m = int(input('输入整数:'))
while m != s:
	if m > s:
		print('大了')
		m = int(input('输入整数:'))
	if m < s:
		print('小了')
		m = int(input('输入整数:'))
	if m == s:
		print('OK')
		break;

'''输出'''
print('100+200+300=', 100+200+300);
print("hello")
print('hhhh')
# name = input()
# print(name)

list = ['runoob',786,2.23,'huangjian']
tinylist = [123, 'john']
print (list);
print(list[1])
print(list[1:])
print(tinylist *2)
print( tinylist+list )

flag = False
name = 'luren'
if name == 'python':         # 判断变量否为'python'
    flag = True          # 条件成立时设置标志为真
    print ('welcome boss')    # 并输出欢迎信息
else:
    print (name)              # 条件不成立时输出变量名称