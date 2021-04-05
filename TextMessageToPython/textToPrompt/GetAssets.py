import os

class Assets:
    def __init__(self):
        self.EMAIL = os.environ.get('PYTHON_EMAIL')
        self.PASSWORD = os.environ.get('PYTHON_EMAIL_PASSWORD')
        self.IMAP_SERVER = 'imap.gmail.com'
        self.SMTP_SERVER = 'smtp.gmail.com'
        self.IMAP_PORT = 993
        self.SMTP_PORT = 465

    def __repr__(self):
        return f'Class Name: {self.__class__.__name__}, System Environment Names Used: PYTHON_EMAIL, PYTHON_EMAIL_PASSWORD, Other Elements Used: {self.SMTP_SERVER} with SSL port {self.SMTP_PORT}, {self.IMAP_SERVER} with SSL port {self.IMAP_PORT}'
