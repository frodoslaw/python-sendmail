#
# eg. of usage
# command: python send-mail.py 'smtp.mycompany.com' '25' 'Subject' 'fromaddr@mail.com' 'toaddr@mail.com' '/tmp/mail.txt'
#

import sys
import smtplib

from email.mime.multipart import MIMEMultipart

smtp_addr = sys.argv[1]
smtp_port = sys.argv[2]
subject = sys.argv[3]
fromaddr = sys.argv[4]
toaddr = sys.argv[5]
file = sys.argv[6]

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = subject

# email body is loaded from file eg. /tmp/mail.txt
filename = file
with open(filename, "rb") as filename:
    text = filename.read()
msg.set_payload(text)

server = smtplib.SMTP(smtp_addr, smtp_port)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
