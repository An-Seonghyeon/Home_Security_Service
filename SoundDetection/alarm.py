import time
import smtplib

TO = '21900421@handong.edu'
GMAIL_USER='an990906@gmail.com'
PASS= 'dks598311'

SUBJECT = 'Alert!'
TEXT = 'Your area is too noisy! Be careful!'

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(GMAIL_USER,PASS)
    header = 'To: ' + TO + '\n' + 'From: ' + GMAIL_USER
    header = header + '\n' + 'Subject: ' + SUBJECT + '\n'
    msg = header + '\n' + TEXT + '\n\n'
    server.sendmail(GMAIL_USER,TO,msg)
    server.quit()
    time.sleep(1)

    
    
