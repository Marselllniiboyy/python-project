# with library SMTPlib Simple Mail Transfer Protocol
import smtplib

# create sesion SMTP connection
s = smtplib.SMTP('smtp.gmail.com', 587)

# For security put SMTP connection in TLS mode (Transport Layer Security)
s.starttls()
print("Connetction Succesfully")

# Authentication
s.login("marseljayawijaya@gmail.com", "bzzi vadf pikw hddw")
print("login sucessfully")
# message 
message = "Bayar utangnya bro"

# sending the mail
s.sendmail("marseljayawijaya@gmail.com", "madetugassma@gmail.com", message)

s.quit()