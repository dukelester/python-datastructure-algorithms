import time
import calendar
import datetime
print(time.time())

#current time

currentTime = time.localtime(time.time())
print("Year => ", currentTime[0]) #year
print("month " , currentTime[1]) #month
print("Day" , currentTime[2]) #day
print(currentTime[3]) #hour
print(currentTime[4]) #minutes

#formatted time

formatted_time = time.asctime(time.localtime(time.time()))
print(formatted_time)

#sleep () ==> a delay
for num in range(0, 5, 2):
    time.sleep(0.2)
    print(num)

# The datetime Module


now = datetime.datetime.now()
print(now)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)
print(datetime.datetime.now().hour)

print(datetime.datetime.today().year)
print(datetime.datetime.timestamp(now))

#create a date object
mydate = datetime.datetime(2022, 4, 9, 9, 58, 50)
print(mydate)

#calender module

cal = calendar.month(2022, 5)
print(cal)

#calender for the whole year
cal_ = calendar.prcal(2022)
print(cal_)
