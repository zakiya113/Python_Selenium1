import datetime
import calendar

x = datetime.datetime.now()

print(x)
print(x.year)
print(x.strftime("%B"))
print(x.strftime("%A"))

y = datetime.datetime(2020,8,19)

print(y)

cal = calendar.month(2017,2)
print(cal)