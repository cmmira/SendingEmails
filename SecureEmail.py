import smtplib, ssl

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_Server = 'smtp.gmail.com'  #Email Server Used
port = 465 # Port Connection needed for SSL and Email Server used

#Email Credentials
user = input("User's Email: ")
password = input("Email Password: ")
recipient = input("Recipient's Email: ")

message = MIMEMultipart("alternative")
message["From"] = user
message["To"] = recipient
message["Subject"] = input("Subject: ")
body = input("Body: ")

# Email Text Version
text = """\
{body}  
""".format(body=body)

# Email HTML Version
html = """\
<html>
    <body>
        <p>
           <strong>{body}</strong> 
        </p>
    </body>
</html>    
""".format(body=body)

# Creating MIMEText Objects for HTML Message
Tmime = MIMEText(text, "plain")
Hmime = MIMEText(html, "html")
message.attach(Tmime)
message.attach(Hmime)


# Load Trusted CA Certificates, Enable Host Name Checking and Certificate Validation,
# Set Secure Protocol and Cipher Settings
context = ssl.create_default_context()
# Commands to Send Emails
with smtplib.SMTP_SSL(SMTP_Server, port, context=context) as server:
    server.login(user, password)
    server.sendmail(user, recipient, message.as_string())
