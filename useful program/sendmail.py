
# https://medium.freecodecamp.org/send-emails-using-code-4fcea9df63f
#
MY_ADDRESS = 'sihaoxiandaixiang@126.com'
MY_PASSWORD = input('Please enter your email Password: ')
#
# Function to read the contacts from a given contact file and return a
# list of names and email addresses
# {'青霞', '曼玉'}
# {'pythonabc@mail.com', 'pythonlink@gmail.com'}
def get_contacts(filename):
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails
#
# to read in a template file (like message.txt) and return a Template object
# made from its contents
from string import Template
#
def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)
#
#
# import the smtplib module. It should be included in Python by default
import smtplib
#
# set up the SMTP server
s = smtplib.SMTP_SSL(host='smtp.126.com', port=465)
# # outlook: s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
# # Gmail: smtp.gmail.com：port (TLS): 587；port (SSL): 465.
#
s.login(MY_ADDRESS, MY_PASSWORD)
#
# to fetch the contact information and the message templates
names, emails = get_contacts('mycontacts.txt')  # read contacts
message_template = read_template('message.txt')
#
#
# send the mail separately
#
# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#
# For each contact, send the email:
for name, email in zip(names, emails):
    msg = MIMEMultipart()       # create a message
#
    # add in the actual person name to the message template
#
    message = message_template.safe_substitute(PERSON_NAME=name.title())
#
    # setup the parameters of the message
    msg['From'] = MY_ADDRESS
    msg['To'] = email
    msg['Subject'] = "群发实验邮件"
#
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))  # send the message via the server set up earlier.
    s.send_message(msg)
#
    del msg
#
# Terminate the SMTP session and close the connection
s.quit()