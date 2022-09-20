# Simple Mail Transfer Protocol
This python project was created to demonstrate the important aspects of the Simple Mail Transfer Protocol that is used to send emails with the email servers. This project demonstrates two methods of sending email using python by creating a secure connection and an unsecure connection.

## Installation and Execution
This python program was created through Windows 10 Visual Studio Code using __Python 3.10.7 64-bit__ from the Microsoft Store and the __Python__ extension from Microsoft.

Installing the code was done using PowerShell and the command:
```powershell
git clone https://github.com/cmmira/SendingEmails.git
```

Running the code was done using Powershell and the command:
```powershell
python3 SecureEmail.py
python3 UnsecureEmail.py
```
When running the code this project uses input from the user to fill out the email credentials and message. While creating this project, Gmail was used but required the creation of an App password in the security settings of the Google profile so that the program can successfully connect to the Email server.

## Creating a Secure Email Connection
The first file __“SecureEmail.py”__ starts by creating a secure connection with the Email server using a TLS encrypted connection.
- For the connection with the Gmail servers using a TLS encrypted connection, the port number needed was __Port 465__ and the email server address __smtp.gmail.com__.
- Input from the terminal was taken to read in the user’s email and password, recipient’s email, email subject, and email message.
- This program also investigated the use of structuring the email with HTTP in order to create a more customized message with the email package in python.
- Using __ssl.create_default_context()__, it created all the important certificates needed to communicate with the Email server, along with choosing the required protocols and cipher settings for the secure connection.
- Finally, using __smtplib.SMTP_SSL()__ the required information was inserted with the assigned variables which allows the command to open, create, and close the connection for a successful email delivery. 

## Creating an Unsecure Email Connection
The second file __“UnsecureEmail.py”__ starts by creating an unsecure SMTP connection and then encrypts it using STARTTLS.
- For a connection with the Gmail server using an unsecure connection and STARTTLS encryption a different port number is required. Port 587 was used with the same email server address __smtp.gmail.com__.
- Input was also taken in from the terminal for the user’s email and password, recipient;s email, email subject, and email message. In this case, the message was designed just by using plain text.
- All the important information was put in variables so that they could be read in while creating the instance __smtplib.SMTP__, which encapsulates an SMTP connection. 
- The __.ehlo()__, is used to identify ourselves to the server and is also done after the __.starttls()__ command.
- The __.starttls__ command is used to encrypt the SMTP connection as an alternative method of sending email while maintaining the security of the contents.

