import smtplib

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

    def sendEmail(self, recipient, message):
        self.smtpconnection.sendmail(self.address, recipient, message)

    def closeSMTP(self):
        self.smtpconnection.close()
