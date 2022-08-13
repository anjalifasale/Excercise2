from datetime import *
present_day=datetime.now()
yesturday=present_day-timedelta(1)
tomarrow=present_day+timedelta(1)

print("yesturday=",yesturday.strftime('%d-%m-%y'))
print("present day=",present_day.strftime('%d-%m-%y'))
print("tommarow=",tomarrow.strftime('%d-%m-%y'))