import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import json

subject = "Tickets | Innovators' Summit"
sender_email = "innovatorssummit01@gmail.com"
password = "Summit@2019"
# password = input("Type your password and press enter:")


def mail(receiver_email, body, att):
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = "Innovators' Summit <innovatorsummit02@gmail.com>"
    # message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    # message["Bcc"] = sender_email  # Recommended for mass emails (sending one email to multiple recepients) Not our case.

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = path  # In same directory as script

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    '''
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )'''

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

if __name__ == "__main__":

    with open('newdata.json') as f:
        data = json.load(f)

    for d in data:
        receiver_email = d['email']

        body1 = '''Hey {},

        Hope you have recieved your ticket. In case you have'nt please do let us know.

Hoping to see you tomorrow at the event.

Regards,
Innovators' Summit 
'''.format(d['name'].title())
        if d['topic'] == "Innovator's Summit Ticket - Track-1 - Student" or d['topic'] == "Innovator's Summit Ticket - Track-1 - Professional":
            body = '''Hi {},

It seems like there was some trouble in sending recent set of tickets.If you have recieved a similar email please ignore this mail.

Thank you for registering for Innovators' Summit. This mail is to confirm that the program will be held as scheduled on 25 January. The registration desk opens at 8:00 am and closes at 9:00 am. The venue for the event is Seminar Complex, Cochin University of Science and Technology. The location for the same is given below.
https://goo.gl/maps/mzMkgdhbhsueZZAM9 

This mail is attached with your event ticket. Please show this ticket at the registration desk.

As you have registered for the Track-1 workshop on "Power of Serverless with AWS Amplify", please bring your laptops with the prerequisite - Nodejs, Amplify CLI (installed and configured), AWS account, VS Code (or any other code editor) and Git. 

CloudSploit is giving away 1 month of Standard service to anyone who registers, with bigger coupons available at the event.
CloudSploit is the leading open source cloud security monitoring service. They've been recognized by SANS and received other accolades by startups and big companies around the world.

For the event to go smoothly you are requested to be at the venue on time.

We have special vouchers for early registrations. Hope we'll see on the event day.

For any queries regarding the event please feel free to contact:

Amal - 8593054259
Alan - 8547963714

Cheers!

Innovators' Summit'''.format(d['name'].title())

        elif d['topic'] == "Student - Workshop ticket":
            body = '''Hi {},

It seems like there was some trouble in sending recent set of tickets.If you have recieved a similar email please ignore this mail.

Thank you for registering for Innovators' Summit. This mail is to confirm that the program will be held as scheduled on 25 January. The registration desk for workshops only opens at 12:30 pm, after which you can have lunch. The venue for the event is Seminar Complex, Cochin University of Science and Technology. The location for the same is given below.
https://goo.gl/maps/mzMkgdhbhsueZZAM9 

This mail is attached with your event ticket. Please show this ticket at the registration desk.

If you want to register for the Track-1 workshop on "Power of Serverless with AWS Amplify", please bring your laptops with the prerequisite - Nodejs, Amplify CLI (installed and configured), AWS account, VS Code (or any other code editor) and Git. 

CloudSploit is giving away 1 month of Standard service to anyone who registers, with bigger coupons available at the event.
CloudSploit is the leading open source cloud security monitoring service. They've been recognized by SANS and received other accolades by startups and big companies around the world.

For the event to go smoothly you are requested to be at the venue on time.

We have special vouchers for early registrations. Hope we'll see on the event day.

For any queries regarding the event please feel free to contact:

Amal - 8593054259
Alan - 8547963714

Cheers!

Innovators' Summit'''.format(d['name'].title())

        else:
            body = '''Hi {},

It seems like there was some trouble in sending recent set of tickets.If you have recieved a similar email please ignore this mail.

Thank you for registering for Innovators' Summit. This mail is to confirm that the program will be held as scheduled on 25 January. The registration desk opens at 8:00 am and closes at 9:00 am. The venue for the event is Seminar Complex, Cochin University of Science and Technology. The location for the same is given below.
https://goo.gl/maps/mzMkgdhbhsueZZAM9 

This mail is attached with your event ticket. Please show this ticket at the registration desk.

CloudSploit is giving away 1 month of Standard service to anyone who registers, with bigger coupons available at the event.
CloudSploit is the leading open source cloud security monitoring service. They've been recognized by SANS and received other accolades by startups and big companies around the world.

For the event to go smoothly you are requested to be at the venue on time.

We have special vouchers for early registrations. Hope we'll see on the event day.

For any queries regarding the event please feel free to contact:

Amal - 8593054259
Alan - 8547963714

Cheers!

Innovators' Summit'''.format(d['name'].title())

        path = 'qr_tickets/' + d['name'] + '.pdf'

        receiver_email = d['email']
        mail(receiver_email, body, path)
        print("Mail sent to", d['name'])