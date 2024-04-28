"""
Gets the email for the recipients and the email and password for the sender.

Also, contains functions for grabbing weekly notes and making weekly emails.

Other functions for taking the weekly notes and grabbing them and making a monthly thing...

"""

import yaml

def read_email_config(yaml_filepath:str):
    """Reads kim's email address"""
    with open(yaml_filepath, 'r') as src:
        yml_dict = yaml.safe_load(src)
        return yml_dict

def parse_weekly_notes(weeks_filepath:str):
    """parses notes from the week stored in the filepath.
    Notes need to be HTML formatted."""






"""
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)

    # Read the image file as binary data
    with open('path/to/your/image.png', 'rb') as img_file:
        img_data = img_file.read()

    # Attach the image as an inline attachment (CID attachment)
    img = MIMEImage(img_data)
    img.add_header('Content-ID', '<my_image>')
    msg.attach(img)

    # Establish the SMTP connection to Gmail's server over a secure SSL connection
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())

    print("Email sent successfully!")

# Example usage
subject = "Weekly Update"
body = "This is the body of the text message with an embedded image."
sender = "your_email@gmail.com"
recipients = ["boss@example.com"]
password = "your_gmail_app_password"  # Generate this in your Google account settings

send_email(subject, body, sender, recipients, password)


"""
### GMAIL API
"""
import os
import base64
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Set up credentials (replace with your credentials file)
creds = None
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

flow = InstalledAppFlow.from_client_secrets_file(
    'path/to/your/credentials.json', SCOPES)
creds = flow.run_local_server(port=0)

# Create Gmail service
service = build('gmail', 'v1', credentials=creds)

# Read the image file as binary data
with open('path/to/your/image.png', 'rb') as img_file:
    img_data = img_file.read()

# Convert binary data to Base64 encoding
img_base64 = base64.urlsafe_b64encode(img_data).decode("utf-8")

# Create the email message
message = {
    'raw': base64.urlsafe_b64encode(
        f"From: your_email@gmail.com\r\n"
        f"To: recipient@example.com\r\n"
        f"Subject: Weekly Update\r\n"
        f"MIME-Version: 1.0\r\n"
        f"Content-Type: text/html; charset=\"utf-8\"\r\n"
        f"<html><body><p>Here's an embedded image:</p>"
        f"<img src='data:image/png;base64,{img_base64}'></body></html>"
        .encode("utf-8")
    ).decode("utf-8")
}

try:
    # Send the email
    service.users().messages().send(userId='me', body=message).execute()
    print("Email sent successfully!")
except HttpError as error:
    print(f"An error occurred: {error}")


"""


# """
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
#
# # Create an HTML email
# msg = MIMEMultipart()
# msg['Subject'] = 'Your Subject'
# msg['From'] = 'sender@example.com'
# msg['To'] = 'recipient@example.com'
#
# # # HTML content
# # html_content = """
# <html>
#     <body>
#         <h1>Hello, World!</h1>
#         <p>This is an embedded image:</p>
#         <img src="cid:my_image">
#     </body>
# </html>
# """

# # Attach the HTML content
# msg.attach(MIMEText(html_content, 'html'))
#
# # Attach the image (replace 'path/to/image.png' with the actual image path)
# with open('path/to/image.png', 'rb') as img_file:
#     img = MIMEImage(img_file.read())
#     img.add_header('Content-ID', '<my_image>')
#     msg.attach(img)
#
# # Send the email using SMTP
# smtp_server = 'your_smtp_server'
# smtp_port = 587
# smtp_username = 'your_username'
# smtp_password = 'your_password'
#
# with smtplib.SMTP(smtp_server, smtp_port) as server:
#     server.starttls()
#     server.login(smtp_username, smtp_password)
#     server.sendmail(msg['From'], msg['To'], msg.as_string())
# """