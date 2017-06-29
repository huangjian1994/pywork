# coding:utf-8  #强制使用utf-8编码格式
# 成功
import smtplib  # 加载smtplib模块
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = 'huangjian8759@163.com'  # 发件人邮箱账号，为了后面易于维护，所以写成了变量
my_user = '857170211@qq.com'  # 收件人邮箱账号，为了后面易于维护，所以写成了变量
#那我去搞企业邮箱
#可以的，去搞个企业邮箱吧

def mail():
    ret = True
    #try:
    msg = MIMEText('你好徐松军，这是测试', 'plain', 'utf-8')
    msg['From'] = formataddr(["173247429@qq.com", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    msg['To'] = formataddr(["857170211@qq.com", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
    msg['Subject'] = "测试邮件"  # 邮件的主题，也可以说是标题

    print('-1')
    server = smtplib.SMTP("smtp.163.com", 25)  # 发件人邮箱中的SMTP服务器，端口是25
    print('0')
    server.login(my_sender, "kphyfhdhbfxtxdzc")  # 括号中对应的是发件人邮箱账号、邮箱密码
    print('1')
    print("这里")
    server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    print("22")
    server.quit()  # 这句是关闭连接的意思
    #except Exception:  # 如果try中的语句没有执行，则会执行下面的ret=False
        #ret = False 验证失败啊   密码是对的 应该是要另外一个密码收件人？ 用授权棉麻试试？ 就是授权密码
    #这就尴尬了，我用QQ的 卡住了？不会啊
    return ret
#可以了，是因为端口么，是的，那我刚刚输入的是登录密码是可以的咯，不一定可以，这是企业邮箱所以才能用这种密码
# 163的需要授权密码，好像QQ的也需要授权密码，这个我知行道，我在其客户端上都要
#

ret = mail()
if ret:
    print("ok")  # 如果发送成功则会返回ok，稍等20秒左右就可以收到邮件
else:
    print("filed")  # 如果发送失败则会返回filed
