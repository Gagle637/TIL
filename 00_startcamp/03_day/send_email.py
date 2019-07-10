import smtplib
from email.message import EmailMessage
import getpass
password = getpass.getpass('PASSWORD : ')
mail_to = ['email_1@naver.com','email_2@naver.com','email_3@naver.com']
for adress in mail_to:   #다중 전송시 5,6번 줄 사용 쉼표 msh['To']에 쉼표 사용하면 다중 전송가능함
    msg = EmailMessage()
    msg['Subject'] = '권고사직서'
    msg['From'] = 'email_1@naver.com'
    msg['To'] = adress
    msg.set_content('죄송합니다..')
    ssafy = smtplib.SMTP_SSL('smtp.naver.com', 465)
    ssafy.login('email_1', password)
    ssafy.send_message(msg)    
print('이메일전송완료')