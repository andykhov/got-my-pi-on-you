import smtplib

#t-mobile: number@tmomail.net

emailServer = "smtp.gmail.com"
emailSender = "johndoe@gmail.com"
emailSenderPass = "johndoepassword"
emailReceiver = "name@email"

smtpserver = smtplib.SMTP(emailServer, 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.login(emailSender, emailSenderPass)
smtpserver.sendmail(emailSender, emailReceiver, "Subject: hello world.\nHi")

smtpserver.quit()
