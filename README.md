# Simple Mail Transfer Protocol
This project uses python to send emails and demonstrate the important aspects of the Simple Mail Transfer Protocol needed to successfully send an email with an Email Client. 
When sending emails there are two common methods of using email commands to connect with an Email Server and send emails to the desired recipient.
- The first file "SecureEmail.py" starts by creating a secure connection with the Email Server using a TLS encrypted connection.  
- The second file "UnsercureEmail.py" starts by creating an unsecure SMTP connection and then encrypts the conenection using the commmand STARTTLS.
- It is also important to note that with this project the sender's email credentials were used from Gmail along with an App password setup in the security settings of the profile. Without this using Gmail credentials did not allow the program to communicate with the Gmail Email Servers.  

## Creating a Secure Email Connection
For this program, the libraries used were important to include in order to use the necessary email commands needed to communicate with the Email Servers. 
- First, it was important to find the port number needed to connect with the Email server address used and the type of encrypted connection used. Port 465 was used since this the number needed for communicating with the Gmail Server and for an Encrypted Connection with SSL.
- Then, input from the terminal was needed to read in the email credentials such as the user's email, user's password, and recipient's email. Input was also taken to create the Subject section of the email and the Body Message of the email.
- Although a simple text could be sent as the body, this program also demostrated the method needed to further customize the message being sent in the email using HTTP. 
- Finally, it was important create the certificates needed to communicate with the Email server so that we are able to identify ourselves to the server. This same function also sets up the required protocols and cipher settings for a secure connection.
- At the end of the program, all the credentials, certificates, and messages for the email could be inserted in smtplib.SMTP_SSL() to open, create, and close the connection for a succcesful email delivery.

## Creating an Unsecure Email Connection
For this program, the important libraries to establish an email connection were used but this time it initiates an unsecure connection with the email server using __.starttls()__. The main difference with this method is that it establishes an unsercure connection first and then encrypts the connection since it is required to have some sort of security with most email servers.
- First, it is important to note that the information required to establish a connection is different with this methods and must use the port number 587 with starttls. The email server still remains the same and all the credentials are read in using standard input.
- Using this information, an instance of smtplib.SMTP is created, which encapsulates an SMTP connection. The __.ehlo()__ is the then used to identify ourselves to the server which is also doen after the __.starttls()__ command.
- The __.starttls()__ command is used to then encrypt the unsecure SMTP connection as an alternative method of sending emails.
- In this program, a try block is used to handle errors with the program so that the code does not crash if something goes wrong and instead does proper error handling.
- The creation of the message to be sent is also styled the same way as when creating a secure email connection since most of the difference is mainly on creating and establishing the connection. 
