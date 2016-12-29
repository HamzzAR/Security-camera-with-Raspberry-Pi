"""
This program sends an email with a picture attached
to it to my personal email.

There is a function below which, i can call from the main file
in order to send the current picture to my email.
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

     
fromaddr = "example@gmail.com"
toaddr = "example2@googlemail.com"
     
msg = MIMEMultipart()
     
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Mr Robot"

     
body = "Hello Sir!\n\nHere is you picture.\nIf there is anything else i can do for you\nPlease let me know Sir.\n\nMr Robot"
     
msg.attach(MIMEText(body, 'plain'))
def send():     
    filename = "pics"
    attachment = open("/home/pi/Desktop/CameraProject/pics/newPic.jpg", "rb")
         
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
         
    msg.attach(part)
         
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "password goes here") 
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print('Email has been sent!')

