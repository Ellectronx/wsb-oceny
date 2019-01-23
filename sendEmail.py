# Import smtplib for the actual sending function
import smtplib
from credent import secret
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
    print("SENDING INFO EMAIL...")
    try:
        server = smtplib.SMTP(secret["smtp_host"], secret["smtp_port"])
        server.ehlo()
        server.login(secret["smtp_login"], secret["smtp_password"])
        server.send_message(msg)
        server.quit()
        print("SENDING OK!")
    except:
        #raise
        print("...sending email: somethin went wrong:(")