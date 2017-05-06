# Load the smtplib

import smtplib

# Create the gmail login crendentials
gmail_user = 'Youremail@gmail.com'
gmail_password = 'yourpassword'


# Create email details
sent_from = 'Youremail@gmail.com'
to = ['email@gmail.com', 'email2@gmail.com']
subject = 'A message sent from pyhton code'
body = 'Hey, whats up with you'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

# Create server for login, send  and close

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print 'Email sent!'
except:
    print 'Something went wrong, fix it!!!'
