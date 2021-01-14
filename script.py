'''
this script demonstrate how to use the api wrapper to get email open rate

'''

# import the class
from api_wrapper import MailStatus

# create email status object
ms = MailStatus(url="https://112b4572b8f2.ngrok.io")

# get unique hash 
i_hash = ms.getHash()
# combine that hash and make a url 
img = ms.getImgURL(i_hash=i_hash)

# this 'll print false if hash is not used
print("status:",ms.hashStatus(i_hash))


# send mail
# import the necessary components first
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# server details
port = 587 
smtp_server = "smtp.gmail.com"
# credentials
from_email = "from@gmail.com"
password = "shhh..!" 
to_email = "to@gmail.com"

# create msg
message = MIMEMultipart("alternative")
message["Subject"] = "Blue Tick Test"
message["From"] = from_email
message["To"] = to_email
# write the HTML part and add the image url
html = '''\
<html>
  <body>
    <p>Hi,<br>
       A 1x1 pixel is here somewhere try and find it! ;)</p>
    <img src="'''+img+'''">
  </body>
</html>
'''
# convert html to MIMEText objects and add them to the MIMEMultipart message
part1 = MIMEText(html, "html")
message.attach(part1)
# send your email
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls()
    server.login(from_email, password)
    server.sendmail(
        from_email, to_email, message.as_string()
    )
 
# open mail using ur email client (Gmail,etc)

# check status this should print True
print("status:",ms.hashStatus(i_hash))

