import smtplib
from typing import Dict
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(to_addrs, body, account_infos: Dict):
    from_addr = login = account_infos.get('user')
    password = account_infos.get('pass')
    
    msg = MIMEMultipart()
    msg['from'] = "confirm_trips@email.com" # Name of the email sender
    msg['to'] = ', '.join(to_addrs)

    msg['Subject'] = "Trip Request Confirmation"
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP(host=account_infos['smtp']['host'],
                          port=account_infos['smtp']['port'])
    server.starttls()
    server.login(login, password)
    text = msg.as_string()
    
    for email in to_addrs:
        server.sendmail(from_addr, email, text)

    server.quit()
