# School Security System Using USB NFC reader

## Introduction
Nowadays, parents are worried about their children because of kidnapping and illegal activities by the children. Parents have long working hours, so they have less time to spend for their children. School has to take responsiblity to look after their students in school time (in-time and out-time) and update the details to their parents.

## Aim of the Project
The aim of this project is to create a security system for the students. This can be achieved by using NFC reader and NFC tags. NFC reader is smartcard reader used to reader the student card(smartcard) and store the details in a text file. Based on the text file an automatic email is send to the parents whose child is late or absent to the school. The student details are stored in MYSQL database. This reduce the worries among the parents regarding their child safety and they also know their child’s attendance details. With the help of SMTP transfer protocol, we can send email to parents.

## Requirements
Database: MySQL,
Domain: Python,
Reader: USB NFC reader(ACR122U),
Smartcards : MIFARE 1K cards,
Simple Mail Transfer Protocal is used to send an email to parents.

## Libraries
Python is an open source library, we can import files from it.For NFC we need to use nfcpy library. For windows we need libUSB and winUSB to use USB NFC reader.
libraries for NFC

## Description
 
The purpose of this project is to track the student’s in time and out time from school. This can be achieved by using NFC reader. 
NFC is a branch of high frequency RFID and both operate at the frequency of 13.56MHz.NFC is designed to be a secure form of data exchange,
and the NFC device is capable of being both an NFC reader and an NFC tag. It can be used for Peer to Peer communication.
 
The NFC reader is placed at the school entrance. For each student a separate Smartcard (ID)s were given. 
Once they entered the school they need to wave or touch the card in the NFC reader. The NFC reader detects the student ID and checks the 
time, if the time is within the limit it marks as present otherwise it marks as absent and stored in separate table (attendance table).

The MYSQL database is used to store the details of the student and the attendance details of each student. 
At the given time the system checks the attendance file, if there is any student absent an email is sent to their parent. To send an email
to the parents, Simple Mail Transfer Protocol (SMTP) is used. 

## Links

The link below expalins the latest nfcpy documentation and how to use it.   
https://buildmedia.readthedocs.org/media/pdf/nfcpy/latest/nfcpy.pdf

The USB NFC reader which i used is shown in the below link:                                 
https://i.ebayimg.com/images/g/oRwAAOSwC~9cRkJZ/s-l300.jpg

#### Note
To run the code, we need USB NFC reader(ACR122U) and MIFARE classic 1K smart cards.

## Sample Output

![image](https://user-images.githubusercontent.com/46959439/69805529-be356580-11d8-11ea-9773-5713a269da34.png)

## Future work

I am planning to create the webpage for school and update the information about the child when their card touches the NFC reader. Through the website parents can login into the system and view their child attendance status (in-time and out-time).
And also I am planning to implement this application in different operating systems. Enabling this application in android, iOS or windows phone, it reduces the carrying of PC or laptop and USB connected NFC reader. The staff can just use their phones to operate the NFC reader.
This application is for ACR122U USB NFC reader. The future work would be extended to check the type of NFC and compatible with other USB NFC reader and smartcards.

## Outcome of adopting this application in school

Reduces the worries among parents (no need to worry about their child in school time) and also the staff who manually monitor the student attendance.
