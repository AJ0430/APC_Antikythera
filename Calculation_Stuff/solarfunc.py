import solarsystem as ss
import datetime
from zoneinfo import ZoneInfo
import astronomy
import math

tz = ZoneInfo("America/New_York")
now    = datetime.datetime.now(datetime.UTC)

def rect2polar(coords):
    return math.degrees(math.atan2(coords[1],coords[0]))

def daylightSavings(year, month, day, hour=12, minute=00):
    dst = datetime.datetime(year, month, day, hour, minute, tzinfo=tz)
    dst = f"{dst.dst()}"
    hours, minutes, seconds = map(int, dst.split(":"))
    return hours

def strip_z(coord):
    return coord[0], coord[1]

def sv_to_coord(state):
    return state.x, state.y
    
def moonphase(year,month,day,hour=12,minute=00):
    current_date = datetime.datetime(year, month, day, hour, minute)
    previous_date = current_date - datetime.timedelta(days=1)
    mooninfo = ss.Moon(year, month, day, hour, minute, -5, daylightSavings(year,month,day,hour,minute), -71.0571, 42.3611, True)
    moonchange = ss.Moon(previous_date.year, previous_date.month, previous_date.day, previous_date.hour, previous_date.minute, -5, daylightSavings(year,month,day,hour,minute), -71.0571, 42.3611, True)
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

def moon(year, month, day, hour=12, minute=00):
    mooninfo = ss.Moon(year, month, day, hour, minute, -5, daylightSavings(year,month,day,hour,minute), -71.0571, 42.3611, True)
    moonpos = mooninfo.position()
    moonpos = strip_z(moonpos)
    return math.degrees(moonpos[1])
    #returns the position of the moon in polar coordinates

def planets(year,month,day,hour=12, minute=00):
    Helio = ss.Heliocentric(year, month, day, hour, minute, 0, 0, 'rectangular', True)
    return Helio.planets()
    #Returns a dictionary of planets and their polar coordinates (X,Y,Z)

def sunriseSet(year, month, day):
    sun = ss.Sunriseset(year, month, day, -5, daylightSavings(year,month,day,12,0), -71.0571, 42.3611)
    return sun.riseset()
    #Returns the sunrise and sunset in decimal time

def JMoons(year, month, day, hour=12, minute=00):
    time = astronomy.Time.Make(year,month,day,hour,minute,0)
    JMooninfo = astronomy.JupiterMoons(time)
    return JMooninfo
    #returns an object containing the positional coordinates of the 4 major moons of jupiter

def Equinox(year):
    return astronomy.Seasons(year)
    #returns an object conaining the four equinoxes of a given year