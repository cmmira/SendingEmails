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

