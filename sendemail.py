import smtplib

#t-mobile: number@tmomail.net

emailServer = "smtp.gmail.com"
emailSender = "andycatpione@gmail.com"
emailSenderPass = "raspberrypi1997"
emailReceiver = "15622902096@tmomail.net"

smtpserver = smtplib.SMTP(emailServer, 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.login(emailSender, emailSenderPass)
smtpserver.sendmail(emailSender, emailReceiver, "Subject: hello world.\nHi")

smtpserver.quit()
