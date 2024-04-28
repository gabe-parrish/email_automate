import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def create_html_email_template(content):
    html_content = f"""
    <html>
    <head>
        <title>Your Email</title>
    </head>
    <body>
        <h1>Hello!</h1>
        <p>{content}</p>
    </body>
    </html>
    """
    return html_content

def send_email(html_content):
    # set up the SMTP server
    s = smtplib.SMTP(host='your_smtp_server', port=587)
    s.starttls()
    s.login('your_username', 'your_password')

    # create a message
    msg = MIMEMultipart('alternative')

    msg['From'] = 'sender_email'
    msg['To'] = 'receiver_email'
    msg['Subject'] = "HTML Email"

    # add in the message body
    msg.attach(MIMEText(html_content, 'html'))

    # send the message via the server set up earlier.
    s.send_message(msg)

    s.quit()

def read_html_file_and_send_email():
    with open('your_file.html', 'r') as f:
        html_file_content = f.read()

    html_email_content = create_html_email_template(html_file_content)

    send_email(html_email_content)

read_html_file_and_send_email()
