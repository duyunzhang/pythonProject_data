import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import *
from email.mime.base import *
from email import encoders

# 地址转换
format_addr = '1572324532@qq.com'
pwd = 'ptopamaybxvxhfbi'
ss=smtplib.SMTP_SSL('smtp.exmail.qq.com',465)
ss.login(format_addr,pwd)

to_addr = input('to:')
# 头文件
msg = MIMEText('带有附件的邮件', 'plain','utf-8')
msg['From'] = Header(f'{format_addr}','utf-8')
msg['To'] = Header(f'{to_addr}','utf-8')
msg['Subject'] = Header('带有附件的邮件','utf-8')




# 正文

# txt = MIMEText('带有附件的邮件,注意查收', 'html', 'utf-8')
# msg.attach(txt)
# # 附件
#
# with open('F:\\pythonProject_data\\html_report\\2022-09-06 19-36-09 report.html', 'rb') as f:
#     mime = MIMEBase('2022-09-06 19-36-09 report','html',filename='2022-09-06 19-36-09 report.html')
#     mime.add_header('Content-Disposition','attachment',filename='2022-09-06 19-36-09 report.html')
#     mime.add_header('Content-ID','<0>')
#     mime.add_header('X-Attachment','0')
#     mime.set_payload(f.read())
#     encoders.encode_base64(mime)

# 建立关联,添加附件
# msg.attach(mime)
# server_host = 'smtp.126.com'
# server = smtplib.SMTP(server_host, 25)
#
# server.login(format_addr, pwd)

ss.sendmail(format_addr, ['1572324532@qq.com'], msg.as_string())

# sender = 'from@runoob.com'
# receivers = ['1572324532@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
#
# #创建一个带附件的实例
# message = MIMEMultipart()
# message['From'] = Header("菜鸟教程", 'utf-8')
# message['To'] =  Header("测试", 'utf-8')
# subject = 'Python SMTP 邮件测试'
# message['Subject'] = Header(subject, 'utf-8')
#
# #邮件正文内容
# message.attach(MIMEText('这是菜鸟教程Python 邮件发送测试……', 'plain', 'utf-8'))
#
# # 构造附件1，传送当前目录下的 test.txt 文件
# att1 = MIMEText(open('F:\\pythonProject_data\\html_report\\2022-09-06 19-36-09 report.html', 'rb').read(), 'base64', 'utf-8')
# att1["Content-Type"] = 'application/octet-stream'
# # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
# att1["Content-Disposition"] = 'attachment; filename="test.txt"'
# message.attach(att1)
#
# # # 构造附件2，传送当前目录下的 runoob.txt 文件
# # att2 = MIMEText(open('runoob.txt', 'rb').read(), 'base64', 'utf-8')
# # att2["Content-Type"] = 'application/octet-stream'
# # att2["Content-Disposition"] = 'attachment; filename="runoob.txt"'
# # message.attach(att2)
#
# try:
#     smtpObj = smtplib.SMTP()
#     smtpObj.sendmail(sender, receivers, message.as_string())
#     print ("邮件发送成功")
# except smtplib.SMTPException:
#     print ("Error: 无法发送邮件")
