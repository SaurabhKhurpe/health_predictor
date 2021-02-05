import smtplib

# Specifying the from and to addresses

fromaddr = 'versatile8474@gmail.com'
toaddrs = 'pawankadadi@gmail.com'

# Writing the message (this message will appear in the email)

msg = '  thank you for joining........welcome  to Bravado health services and disease prediction '

# Gmail Login

username = 'versatile8474@gmail.com'
password = '8421348474'

# Sending the mail

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
