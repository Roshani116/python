from datetime import datetime
import time
#before importing datetime class code looks like below after importing date time class c
#dt= datetime.datetime(2018,1,1)
#after importing datetime class.
dt1 = datetime(2018,1,1)
dt2 = datetime.now()
dt = datetime.strptime("2018/01/01", "%Y/%m/%d")
#we can get in python 3 strptime meaning of each character there %Y/%m/%d
dt = datetime.fromtimestamp(time.time())
print(dt)
#our datetiem object have attributes like year month day and so on
print(f"{dt.year}/{dt.month}")
#strftime method is opposite from strptime as strptime a string into a date time object but with strftime we convert a date 
#time object into string
print(dt.strftime("%y/%m"))
print(dt2>dt1)



