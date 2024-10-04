import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os


def send_email_with_attachment(smtp_server, smtp_port, email_address, email_password, subject, body, file_path):
    """
    
    Sends an email with the specified file attached.

    Args:
        smtp_server (str): The SMTP server address.
        smtp_port (int): The SMTP server port.
        email_address (str): The sender's email address.
        email_password (str): The sender's email password.
        subject (str): The subject of the email.
        body (str): The body of the email.
        file_path (str): The path to the file to attach.
    """
