import smtplib
EMAIL_ADDRESS="" #YOUR EMAIL
PASSWORD="" #YOUR PASSWORD FOR EMAIL

#MAKE SURE TO ENABLE LESS SECURE APPS ON GOOGLE

def send_mail(msg, mail):
      server = smtplib.SMTP('smtp.gmail.com', 587)
      server.ehlo()
      server.starttls()
      server.login(EMAIL_ADDRESS, PASSWORD)
      server.sendmail(EMAIL_ADDRESS, mail, msg)
