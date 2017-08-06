import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

class email:

    emailCount = 0;

    def __init__(self, address, password):
        self.address = address
        self.password = password
        email.emailCount += 1

    def initSMTP(self, emailserver, port):
        self.smtpconnection = smtplib.SMTP(emailserver, port) #returns an SMTP object
        self.smtpconnection.ehlo() #says "hello" to smtp server
        self.smtpconnection.starttls() #enable TLS encryption
        self.smtpconnection.login(self.address, self.password)

    def sendEmail(self, recipient, subject, message, imgPath):
        msg = MIMEMultipart()
        msg["Subject"] = subject
        msg["From"] = self.address
        msg["To"] = recipient
        msg.attach(MIMEText(message))
        
        imgfp = open(imgPath, "rb")
        img = MIMEImage(imgfp.read())
        imgfp.close()
        msg.attach(img)

        self.smtpconnection.sendmail(self.address, recipient, msg.as_string())

    def closeSMTP(self):
        self.smtpconnection.close()
