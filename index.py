import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = 'eugeneasande999@gmail.com'
sender_password = '6vL3HAYSgqKmxEw7'
receiver_email = 'famaso.fmks@gmail.com', 'eugzasax@outlook.com'
subject = 'GREETINGS'
message = 'Welcome to FAMASO. This is an online platfor to connect buyers with farmers. This is a test'

# Create a message container (MIMEMultipart object)
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Attach the message to the MIMEMultipart object
msg.attach(MIMEText(message, 'plain'))

# Establish a connection to the SMTP server (Gmail in this example)
try:
    smtp_server = smtplib.SMTP('smtp-relay.brevo.com', 587)
    smtp_server.starttls()  # Start TLS encryption
    smtp_server.login(sender_email, sender_password)
except Exception as e:
    print(f"Failed to connect to the SMTP server: {e}")
    exit()

# Send the email
try:
    smtp_server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")

# Close the SMTP server connection
smtp_server.quit()
