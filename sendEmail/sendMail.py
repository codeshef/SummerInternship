import smtplib

# use SMTP of smtplib to send email

server = smtplib.SMTP("smtp.gmail.com", 587)

# contract with Gmail

server.starttls()
server.login('hqmssystem@gmail.com', 'hqms_123 ')

# contains senderMail,receiverMail,Message
server.sendmail('hqmssystem@gmail.com', 'hqmssystem@gmail.com', "Hello Python!!!")

print("Yiepiee email send successfully!!!")
