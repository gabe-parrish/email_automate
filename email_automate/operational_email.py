"""
Sends out a daily message. If the day is an email day i.e.
Friday morning or the first of the month,
the appropriate email updates are sent based on this script.
"""
from email_automate.configurator import read_email_config
from weekly_email_kim import send_email, create_msg, embed_images_n_html_markup


def runs():

    path = r'C:\Users\gparrish\Documents\updates\parameters\kim_email_dets.yml'
    yml_dict = read_email_config(yaml_filepath=path)
    print(yml_dict)

    test_email = r'C:\Users\gparrish\Documents\updates\Notes\weekly\test_week_1\email_text.txt'

    lines = []
    with open(test_email, 'r') as src:
        for l in src:
            lines.append(l.rstrip())

    # ## todo - process email and embed the images necessary
    embed_images_n_html_markup(html_content=lines, working_location=test_email, cfg=yml_dict)

if __name__ == "__main__":
    runs()