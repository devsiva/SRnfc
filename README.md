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
Python is an open source library, we can import files from it.For NFC we need to use nfcpy library. 
### Windows 
For windows we need WinUSB and libUSB. 
### Date and time
import date and time for current date and time
### SMTP
import smtplib is a library for SMTP. We can retrieve files from it.
## Installations
   ### To install libUSB(windows)
  • Download libusb (Downloads -> Latest Windows Binaries). 
  
. • For 32-bit Windows: – Copy MS32\dll\libusb-1.0.dll to C:\Windows\System32.
After installing the WinUSB and libUSB we need to install latest version of python.

### Python and NFCpy
Python 2.7 is used in this poject,because NFC is not supported by python 3. Once python is installed use pip method to install latest version of NFCpy.

$ Pip install -U nfcpy

Then we need to configure the path, otherwise we cannot access the pip in command line.     
For example, C:/python2.7/scripts/pip.exe

### Database
import mysql.connector

MySQL connector used to connect the python and MySQL.

## For Implementation
See the Libraries for NFC file and nfc.py file in this repository

## Links

The link below expalins the latest nfcpy documentation and how to use it.   
https://buildmedia.readthedocs.org/media/pdf/nfcpy/latest/nfcpy.pdf

The USB NFC reader which i used is shown in the below link:                                 
https://i.ebayimg.com/images/g/oRwAAOSwC~9cRkJZ/s-l300.jpg

#### Note
To run the code, we need USB NFC reader(ACR122U) and MIFARE classic 1K smart cards.
The sender email account is set to less secure. i.e turn on less secure app in setting otherwise an email cannot send to parents.
The gmail account is used.

## Sample Output

![image](https://user-images.githubusercontent.com/46959439/69805529-be356580-11d8-11ea-9773-5713a269da34.png)

## Future work

I am planning to create the webpage for school and update the information about the child when their card touches the NFC reader. Through the website parents can login into the system and view their child attendance status (in-time and out-time).
And also I am planning to implement this application in different operating systems. Enabling this application in android, iOS or windows phone, it reduces the carrying of PC or laptop and USB connected NFC reader. The staff can just use their phones to operate the NFC reader.
This application is for ACR122U USB NFC reader. The future work would be extended to check the type of NFC and compatible with other USB NFC reader and smartcards.

## Outcome of adopting this application in school

Reduces the worries among parents (no need to worry about their child in school time) and also the staff who manually monitor the student attendance.
