# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage


def sendEmail(subject,eml_from,eml_to,message):
    # Open the plain text file whose name is in textfile for reading.

    msg = EmailMessage()
    msg.set_content(message)

    msg['Subject'] = subject
    msg['From'] = eml_from
    msg['To'] = eml_to

    # Send the message via our own SMTP server.
    print("PRÓBA WYSYŁKI:")
    server = smtplib.SMTP('smtp.mail.pl',587)
    server.ehlo()
    server.login('auto@danilewicz.com', 'ra2tSGQieSiRo47P')
    server.send_message(msg)
    server.quit()