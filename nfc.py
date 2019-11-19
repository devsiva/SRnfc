#importing python libraries

import nfc
import time
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import mysql.connector

#Connecting the database with the python 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="staff"
)

#Getting the current date and time to check the student in-time
mycursor = mydb.cursor()
currentDT = datetime.datetime.now()
vk = currentDT.strftime("%Y-%m-%d %H:%M:%S")
print (vk)


def after5s(started):

    return time.time() - started > 20


def read():

    clf = nfc.ContactlessFrontend('usb')

    def after5s(): return time.time() - started > 20
    started = time.time()
    #prints the usb and its device and bus number and terminates after 5sec
    tag = clf.connect(rdwr={'on-connect': lambda tag: False}, terminate=after5s)

    tag = str(tag)

    tag = tag.split(" ")[-1] 
    #print(tag) #prints id of the tag

    return tag[3:-1]#stripping the last digit in the ID
   


if __name__ == '__main__':

    tag =read()
    print(tag)
    #updating tag details in the database
    sql="update tag set datetime='"+vk+"' where tag='"+tag+"' "
    mycursor.execute(sql)
    mydb.commit()

mycursor.execute("SELECT * FROM tag where tag='"+tag+"' ")

tag = mycursor.fetchall()

for x in tag:
    id = x[0]
    print(id)
    name=x[2]
    print(name)
    email=x[4]
    print (email)
    t1 = x[5]
      
 #gmail account is used here   
email_user = 'ssr19.bbk@gmail.com' #sender email id
email_password = 'student@bbk'     #sender password
email_send = email                 #receiver email

subject = 'subject'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject
#message sent to parent
body = 'Dear Parent \n Your child : '+name+ ' is Late and marked as absent for morning session'
msg.attach(MIMEText(body,'plain'))

text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)

#checks student in-time with the given time
if currentDT.hour >= 10:
    print(" Late and marked as absent for morning session") 
    server.sendmail(email_user,email_send,text)
server.quit()
   
