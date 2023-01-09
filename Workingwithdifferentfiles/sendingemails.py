from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

template = Template(path("workingwithTemplates.html")).read_text())

message = MIMEMultipart()
message["from"] = "ssharmaroshani116@gmail.com"
message["to"] = "ssharmaroshani116@gmail.com"
message["subject"] = "This is a test"
template.substitute({"name" : "John"})
#for body of email
message.attach(MIMEText("Body"))
# now we need to send this using smtp server

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("ssharmaroshani116@gmail.com", "Roshani@116901")
    smtp.send_message(message)
    print("sent..")


