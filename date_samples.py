from datetime import datetime

# print(datetime.datetime.now())
now = datetime.now()
print(now)
print(datetime.timestamp(now))

print(now.strftime("%Y%m%d%H%M%S"))
