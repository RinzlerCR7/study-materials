import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body, to_email):
    # SMTP server configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_user = "souravmahatocr7@gmail.com"
    smtp_password = "zpcguilqlchnlrlc"

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'html'))

    # Connect to the SMTP server and send the email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, to_email, msg.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Example usage
send_email("Test Subject", "<h1>This is an HTML email</h1>", "somahato@deloitte.com")
