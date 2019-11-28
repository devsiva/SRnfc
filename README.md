Hi, 
I am Sivagami.

Here I am going to discuss about my project, which is School Security System using NFC reader and its a prototype project.

Requirements:

Database: MySQL,
Domain: Python,
Reader: USB NFC reader(ACR122U),
Smartcards : MIFARE 1K cards,
Simple Mail Transfer Protocal is used to send an email to parents.

Description:
 
The purpose of this project is to track the student’s in time and out time from school. This can be achieved by using NFC reader. 
NFC is a branch of high frequency RFID and both operate at the frequency of 13.56MHz.NFC is designed to be a secure form of data exchange,
and the NFC device is capable of being both an NFC reader and an NFC tag. It can be used for Peer to Peer communication.
 
The NFC reader is placed at the school entrance. For each student a separate Smartcard (ID)s were given. 
Once they entered the school they need to wave or touch the card in the NFC reader. The NFC reader detects the student ID and checks the 
time, if the time is within the limit it marks as present otherwise it marks as absent and stored in separate table (attendance table).

The MYSQL database is used to store the details of the student and the attendance details of each student. 
At the given time the system checks the attendance file, if there is any student absent an email is sent to their parent. To send an email
to the parents, Simple Mail Transfer Protocol (SMTP) is used. 

The link below expalins the latest nfcpy documentation and how to use it.   
https://buildmedia.readthedocs.org/media/pdf/nfcpy/latest/nfcpy.pdf

The USB NFC reader which i used is shown in the below link: 
https://i.ebayimg.com/images/g/oRwAAOSwC~9cRkJZ/s-l300.jpg

Note:
To run the code, we need USB NFC reader(ACR122U) and MIFARE classic 1K smart cards.

Sample Output:

2019-11-28 10:30:28        # Date and Time

6CC6FD2	                   #	Smart card ID

3			                       # Register number where details of the students are stored 

Kreethi		                  #	Name of the student

sivagamink@gmail.com       # Parent email-id

Late and marked as absent for morning session  # Message sent to parent

Future work:

I am planning to create the webpage for school and update the information about the child when their card touches the NFC reader. Through the website parents can login into the system and view their child attendance status (in-time and out-time).
And also I am planning to implement this application in different operating systems. Enabling this application in android, iOS or windows phone, it reduces the carrying of PC or laptop and USB connected NFC reader. The staff can just use their phones to operate the NFC reader.
This application is for ACR122U USB NFC reader. The future work would be extended to check the type of NFC and compatible with other USB NFC reader and smartcards.

Outcome of adopting this application in school,  reduces the worries among parents (no need to worry about their child in school time) and also the staff who manually monitor the student attendance.
