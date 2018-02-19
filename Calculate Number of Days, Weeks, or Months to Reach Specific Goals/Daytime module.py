import datetime
import pytz #for timezone

d=datetime.date(2016,7,24)
print(d)
tday=datetime.date.today()
print(tday)
print(tday.year)
print(tday.weekday()) #MONDAY 0 Sunday 6
print(tday.isoweekday()) #Monday 1 sunday 7

tdelta=datetime.timedelta(days=7) #time duration
print(tday+tdelta)
print(tday-tdelta)

#birthday
bday=datetime.date(2018,8,10) #only date
till_bday=bday-tday
print(till_bday.days)
print(till_bday.total_seconds())

t=datetime.time(12,30,45,100)  #only hour/minute/second
print(t)

t=datetime.datetime(2018,8,10,12,30,45,100) #everything!

tdelta=datetime.timedelta(hours=7)
print(t+tdelta)

dt = datetime.datetime(2018,8,10,12,30,45,tzinfo=pytz.UTC)
print(dt)
dt_utcnow=datetime.datetime.now(tz=pytz.UTC)  #世界协调时间
print(dt_utcnow)

dt_mtn=dt_utcnow.astimezone(pytz.timezone('Canada/Eastern'))
print(dt_mtn.isoformat()) #standard format time display
print(dt_mtn.strftime('%B %d, %Y')) #change datetime to string


#for tz in pytz.all_timezones: #search timezones
#    print(tz)

dt_mtn=datetime.datetime.now()
print(dt_mtn)
 #change string to datetime
dt_str='February 16, 2018'
dt=datetime.datetime.strptime(dt_str, '%B %d, %Y')
