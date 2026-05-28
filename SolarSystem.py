import solarsystem as ss
import datetime

now    = datetime.datetime.utcnow()
now    = datetime.datetime.now(datetime.timezone.utc)
year   = now.year
month  = now.month
day    = now.day
hour   = now.hour
minute = now.minute

mooninfo = ss.Moon(year,month,day,hour,minute,0,0,0,51.5,True)
moonchange = ss.Moon(year, month, day-1, minute, 0, 0, 0, 51.5, True)
phase = ""
print(mooninfo.phase())
if(mooninfo.phase()> moonchange.phase()):
    phase = "Waxing"
else:
    phase = "Waning"
print(phase)
moontype = ""
if(round(mooninfo.phase(),1) == 0.5):
    moontype = "Half Moon"
elif(round(mooninfo.phase(),2) < 0.1):
    moontype = "New Moon"
elif(round(mooninfo.phase(),2) > 0.9):
    moontype = "Full Moon"
elif(round(mooninfo.phase(),2) > 0.5):
    moontype = "Gibbous"
elif(round(mooninfo.phase(),2) < 0.5):
    moontype = "Crescent"

print(moontype)
