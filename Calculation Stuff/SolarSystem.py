import solarsystem as ss
import datetime
from zoneinfo import ZoneInfo
import astronomy
import matplotlib.pyplot as plt

tz = ZoneInfo("America/New_York")
now    = datetime.datetime.now(datetime.UTC)



def daylightSavings(year, month, day, hour, minute):
    dst = datetime.datetime(year, month, day, hour, minute, tzinfo=tz)
    dst = f"{dst.dst()}"
    hours, minutes, seconds = map(int, dst.split(":"))
    return hours
    
def moonphase(year,month,day,hour,minute):
    mooninfo = ss.Moon(year, month, day, hour, minute, -5, daylightSavings(year,month,day,hour,minute), -71.0571, 42.3611, True)
    moonchange = ss.Moon(year, month, day-1, hour, minute, -5, daylightSavings(year,month,day,hour,minute), -71.0571, 42.3611, True)
    phase = ""
    if(mooninfo.phase() > moonchange.phase()):
        phase = "Waxing"
    else:
        phase = "Waning"
    moontype = ""
    if(round(mooninfo.phase(),1) == 0.5):
        moontype = "Half Moon"
    elif(round(mooninfo.phase(),2) < 0.1):
        moontype = "New Moon"
    elif(round(mooninfo.phase(),2) > 0.99):
        moontype = "Full Moon"
    elif(round(mooninfo.phase(),2) > 0.5):
        moontype = "Gibbous"
    elif(round(mooninfo.phase(),2) < 0.5):
        moontype = "Crescent"
    phaselist = [phase, moontype]
    return phaselist
    #Returns an array with the whether the moon is waxing or waning, and the current phase of the moon

def moon(year, month, day, hour, minute):
    mooninfo = ss.Moon(year, month, day, hour, minute, -5, daylightSavings(year,month,day,hour,minute), -71.0571, 42.3611, True)
    moonpos = mooninfo.position()
    moonpos = ss.spherical2rectangular(moonpos[0],moonpos[1],moonpos[2])
    return moonpos
    #returns the position of the moon in rectangular coordinates

def planets(year,month,day,hour,minute):
    Helio = ss.Heliocentric(year, month, day, hour, minute, 0, 0, 'rectangular', True)
    return Helio.planets()
    #Returns a dictionary of planets and their rectangular coordinates (X,Y,Z)

def sunriseSet(year, month, day):
    sun = ss.Sunriseset(year, month, day, -5, daylightSavings(year,month,day,12,0), -71.0571, 42.3611)
    return sun.riseset()
    #Returns the sunrise and sunset in decimal time

def JMoons(year, month, day, hour, minute):
    time = astronomy.Time.Make(year,month,day,hour,minute,0)
    JMooninfo = astronomy.JupiterMoons(time)
    return JMooninfo
    #returns an object containing the positional coordinates of the 4 major moons of jupiter

def Equinox(year):
    return astronomy.Seasons(year)
    #returns an object conaining the four equinoxes of a given year

print(moonphase(now.year,now.month,now.day,now.hour,now.minute))
Hh = planets(now.year,now.month,now.day,now.hour,now.minute)
for key, value in Hh.items():
    print(f"{key},{value}")
print(moon(now.year,now.month,now.day,now.hour,now.minute))
print(sunriseSet(now.year,now.month,now.day))
jmoons = JMoons(now.year,now.month,now.day,now.hour,now.minute)
eq = Equinox(2026)
print(eq.mar_equinox)
print(f"{jmoons}")