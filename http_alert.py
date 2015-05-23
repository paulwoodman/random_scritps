#!/usr/bin/python
# http status check for a site
# if code is not 200 then a email will be sent

import requests
import smtplib
import threading

http = 'http://www.example.com'
msg = 'Service unavailable'
username = 'smtp username'
password = 'smtp password'

def get_response():
    r = requests.get(http)
    if r.status_code == 200:
      print 'no issues, no email needed' 
    else:
      return alert_email()

def alert_email():
    server = smtplib.SMTP('your_smtp_relay_server', relay_port_number)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail('sender.email.com', 'to.email_address.com', msg)
    server.quit()

def recurring():
    get_response()
    threading.Timer(10, recurring).start()

recurring()



