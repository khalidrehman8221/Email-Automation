import smtplib


to = input("Enter the email address of the reciver :-")

message = input("Enter the message :-")

def sendEmail(to, message);
   sever = smtplib.SMTP('smtp.gamil.com',587)
   sever.starttls()
   sever.login('senderemail','password')
   server.sendmail(senderemail, to, message)
   sever.close()

sendEmail(to, message)  