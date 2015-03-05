import smtplib,location, time

from email.mime.text import MIMEText
# SMTP-сервер
server = "ServerAdress"
port = 22 # Станартный порт
user_name = "test1@site.com"
user_passwd = "Password"
send_name='test2@site.com'

s = smtplib.SMTP(server, port)
s.ehlo()
s.starttls()
s.ehlo()
s.login(user_name, user_passwd)

location.start_updates()
time.sleep(10)
location.stop_updates()
loc = location.get_location()
addr = location.reverse_geocode(loc)[0]



Text ='Я нахожусь по адресу: ' + addr['Country'] + ', город ' + addr['City']+', ' + addr['Name']

letter = MIMEText(Text,'html','utf-8')
letter['Subject']= 'Текущая геолокация'
letter['To']=send_name
letter=letter.as_string()
s.sendmail(user_name,send_name,letter)
s.close