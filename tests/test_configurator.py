import pytest
from email_automate.configurator import read_email_config

test_path = 'test_files/test_yaml.yml'

def test_read_email_config():
    email_dict = read_email_config(test_path)
    assert(email_dict['my_email'] == 'myself@team.com')