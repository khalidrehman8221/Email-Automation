import smtplib


to = input("Enter the email address of the reciver :-")

message = input("Enter the message :-")

def sendEmail(to, message);
   server = smtplib.SMTP('smtp.gamil.com',587)
   server.starttls()
   server.login('senderemail','password')
   server.sendmail(senderemail, to, message)
   server.close()

sendEmail(to, message)  
