import time
#print(time.time())
# function to send the email to 10000 receipients
def send_emails():
    for i in range(800000):
        pass

start= time.time()
send_emails()
End= time.time()
duration= End- start
print(duration)