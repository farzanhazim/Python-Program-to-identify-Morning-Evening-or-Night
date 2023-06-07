import time
timestamp = time.strftime('%H,%M,%S')
print(timestamp)
hour = int(time.strftime('%H'))
minute = int(time.strftime('%M'))
second = int(time.strftime('%S'))

if (hour > 12 <12 ):
    print("Morning")
elif (hour > 12 < 5):
    print("Evening")
else:
    print("Night")
