import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration - set default to gmail
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = ''
EMAIL_PASSWORD = ''

def send_email(subject, message, to):
    # mime multipart object allows you to mimic email structure
    msg = MIMEMultipart()
    #email address of sender
    msg['From'] = EMAIL_ADDRESS
    # email address of recipient 
    msg['To'] = to
    msg['Subject'] = subject

    # adding in message
    msg.attach(MIMEText(message, 'plain'))

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)


def main():
   # Making list of recipients
    recipients = ['aupadhy@gmail.com']

    #Sending a message to each recipient in list
    for recipient in recipients:
        subject = 'Test Email'
        message = 'Sent via Python'
        send_email(subject, message, recipient)
        print('Email sent to:', recipient)

if __name__ == '__main__':
    main()
