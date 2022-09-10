import smtplib, ssl

SMTP_Server = 'smtp.gmail.com' # Email Server
port = 587 # Port Connection with StartTLS

# Email Credentials
user = input("User's Email: ")
password = input("Password: ")
recipient = input ("Recipient's Email: ")

Subject = input("Subject: ")
Body = input ("Body: ")

message = """\
From:{user}
To:{recipient}
Subject: {Subject}

{Body}""".format(user=user,recipient=recipient,Body=Body,Subject=Subject)

context = ssl.create_default_context()
with smtplib.SMTP(SMTP_Server, port) as server:
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(user, password)
    server.sendmail(user, recipient, message)
