import astronomy 


def JMoons(year, month, day, hour, minute):
    time = astronomy.Time.Make(year,month,day,hour,minute,0)
    JMooninfo = astronomy.JupiterMoons(time)
    return JMooninfo

def Equinox(year):
    return astronomy.Seasons(year)

jmoons = JMoons(2026,6,11,11,41)
print(jmoons.io.x, jmoons.io.y)
eq = Equinox(2026)
print(eq.mar_equinox)
    
