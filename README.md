Hi, 
I am Sivagami.

Here I am going to discuss about my project, which is School Security System using NFC reader and its a prototype project.

Requirements:

Database: MySQL,
Domain: Python,
Reader: USB NFC reader(ACR122U),
Smartcards : MIFARE 1K cards,
Simple Mail Transfer Protocal is used to send an email to parents.

Despription:
 
The purpose of this project is to track the student’s in time and out time from school. This can be achieved by using NFC reader. 
NFC is a branch of high frequency RFID and both operate at the frequency of 13.56MHz.NFC is designed to be a secure form of data exchange,
and the NFC device is capable of being both an NFC reader and an NFC tag. It can be used for Peer to Peer communication.
 
The NFC reader is placed at the school entrance. For each student a separate Smartcard (ID)s were given. 
Once they entered the school they need to wave or touch the card in the NFC reader. The NFC reader detects the student ID and checks the 
time, if the time is within the limit it marks as present otherwise it marks as absent and stored in separate table (attendance table).

The MYSQL database is used to store the details of the student and the attendance details of each student. 
At the given time the system checks the attendance file, if there is any student absent an email is sent to their parent. To send an email
to the parents, Simple Mail Transfer Protocol (SMTP) is used. 

