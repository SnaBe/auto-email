# Needed libraries
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import details

# Variables
my_email_address = details['email_address']
my_email_password = details['email_password']
email_list = details['users']
email_body = details['message']

msg = MIMEMultipart()
msg['Subject'] = details['subject']

msg.attach(MIMEText(email_body, 'plain'))

# Gmail email server
server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

# Login into the email server
server.login(my_email_address, my_email_password)

email_content = msg.as_string()

# Send an email for each user in our list
server.sendmail(my_email_address, email_list, email_content)

server.quit()

print('Emails sent!')
