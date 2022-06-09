#!C:\Users\Nika_Lis\AppData\Local\Programs\Python\Python37\python.exe
# 5. Написать серверный сценарий, который отправляет почту
import cgi
import smtplib
from email.mime.text import MIMEText

form = cgi.FieldStorage()

emailFrom = form["emailFrom"].value
tokenFrom = form["tokenFrom"].value
emailTo = form["emailTo"].value
message = "Сообщение для отправления на почту"
msg = MIMEText(message, 'plain', 'utf-8')
msg['Subject'] = "Тема письма"

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()
smtpObj.login(emailFrom, tokenFrom)
smtpObj.sendmail(emailFrom, emailTo, msg.as_string())
smtpObj.quit()
