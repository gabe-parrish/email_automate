import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from configurator import read_email_config
import os

def create_msg(message:str):
    """create that dang message"""
    html_content = f"""
    <html>
    <head>
        <title>Weekly Update</title>
    </head>
    <body>
        <h1>Hi Kim, Here are my updates from this week: </h1>
        {message}
    </body>
    </html>
    """

    print('the content:\n', html_content)

    return html_content

def email_kim(date:str, yaml_fp:str):

    email_params = read_email_config(yaml_filepath=yaml_fp)

    # Open the files in binary mode
    with open('email_content.txt', 'rb') as txtfile, open('image.jpg', 'rb') as imgfile:
        msg = MIMEMultipart()
        msg['From'] = 'your-email@gmail.com'
        msg['To'] = 'recipient-email@gmail.com'

        # Read the content of the text file
        txt = txtfile.read().decode()
        msg['Subject'] = txt.splitlines()[0]  # Subject is the first line
        body = '\n'.join(txt.splitlines()[1:])  # The rest is the body
        msg.attach(MIMEText(body, 'html'))  # Use 'html' instead of 'plain'

        # Read the content of the image file
        img = MIMEImage(imgfile.read())
        img.add_header('Content-ID', '<image1>')  # If needed, add headers
        msg.attach(img)

    # Send the email via Gmail's SMTP server on port 587
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()

    # Login to your Gmail account
    smtp.login('your-email@gmail.com', 'your-password')

    # Send the email
    smtp.send_message(msg)
    smtp.quit()

def send_email(html_content, cfg):
    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(cfg['my_email'], cfg['my_pass'])

    # create a message
    msg = MIMEMultipart('alternative')

    msg['From'] = cfg['my_email']
    msg['To'] = cfg['recipient']
    msg['Subject'] = "weekly update test"

    # add in the message body
    msg.attach(MIMEText(html_content, 'html'))

    print(cfg['my_email'], )

    # send the message via the server set up earlier.
    s.send_message(msg)

    s.quit()

def embed_images_n_html_markup(html_content:list, working_location:str, cfg:dict):
    """Parses the html and grabs images from the working location"""

    # create a message
    msg = MIMEMultipart('alternative')
    # msg = MIMEMultipart()

    msg['From'] = cfg['my_email']
    msg['To'] = cfg['recipient']
    msg['Subject'] = "weekly update test"

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(cfg['my_email'], cfg['my_pass'])

    # ==== parse the message ====
    loc = os.path.split(working_location)[0]
    img_loc = os.path.join(loc, 'images')
    print(img_loc)
    image_paths = []
    image_names = []
    html_lines = []
    for line in html_content:
        # print(line)
        if line.startswith('['):
            print(f'{line} should be an image')
            img_name = line.replace('[', '').replace(']', '')
            l_img_path = os.path.join(img_loc, f'{img_name}.png')
            image_paths.append(l_img_path)
            image_names.append(img_name)
            corr_line = f"<img src='cid:{img_name}'>"
            html_lines.append(corr_line)
        else:
            print(f'{line} \n should be a paragraph')
            newline = f'<p>{line}</p>'
            html_lines.append(newline)

    joined_html = '\n'.join(html_lines)
    final_email = create_msg(message=joined_html)
    # Attach the HTML content
    msg.attach(MIMEText(final_email, 'html'))
    # attach the photos corresponding to names in html.
    for img, n in zip(image_paths, image_names):
        print('image path is: ', img)
        print('n is:', n)
        with open(img, 'rb') as img_file:
            mimg = MIMEImage(img_file.read())
            mimg.add_header('Content-ID', f'<{n}>')
            msg.attach(mimg)

    # send the message via the server set up earlier.
    s.send_message(msg)

    s.quit()

