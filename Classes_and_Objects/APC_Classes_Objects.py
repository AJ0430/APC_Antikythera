import sqlite3

# tells the program to connect to the database and creates a cursor to execute commands
conn = sqlite3.connect("Database_Stuff/AntikytheraSystem.db")
cursor = conn.cursor()

# creates a base class called SolarBodies with the common attributes of all solar bodies
class solarBodies:
    def __init__(self, name, mass, radius, gravitationalPull, orbitalPosition):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.gravitationalPull = gravitationalPull
        self.orbitalPostion = orbitalPosition

# creates a subclass called Planets that inherits from SolarBodies and has additional attributes specific to planets
class planets(solarBodies):
    def __init__(self, name, mass, radius, gravitationalPull, orbitalPosition, type, surfaceTemp, sunDistance, moons, period):
        super().__init__(name, mass, radius, gravitationalPull, orbitalPosition)
        self.type = type
        self.surfaceTemp = surfaceTemp
        self.sunDistance = sunDistance
        self.moons = moons
        self.period = period

    # function to print all the information about the planet in a readable format
    def printInfo(self):
        print(f'Name: {self.name}')
        print(f'Mass: {self.mass} kg')
        print(f'Radius: {self.radius} km')
        print(f'Gravitational Pull: {self.gravitationalPull} m/s^2')
        print(f'Orbital Position: {self.orbitalPostion}')
        print(f'Type: {self.type}')
        print(f'Surface Temperature: {self.surfaceTemp} C')
        print(f'Distance from Sun: {self.sunDistance} AU')
        print(f'Number of Moons: {self.moons}')
        print(f'Orbital Period: {self.period} Earth Years')

#creates a subclass called Moons that inherits from SolarBodies and has additional attributes specific to moons
class moons(solarBodies):
    def __init__(self, name, mass, radius, gravitationalPull, orbitalPosition, planetOrbiting):
        super().__init__(name, mass, radius, gravitationalPull, orbitalPosition)
        self.planetOrbiting = planetOrbiting

    # function to print all the information about the moon in a readable format
    def printInfo(self):
        print(f'Name: {self.name}')
        print(f'Mass: {self.mass} kg')
        print(f'Radius: {self.radius} km')
        print(f'Gravitational Pull: {self.gravitationalPull} m/s^2')
        print(f'Orbital Position: {self.orbitalPostion}')
        print(f'Planet Orbiting: {self.planetOrbiting}')
# Create a list used to store the moon objects, create an object for each moon using data from the MOONS table in the database, then st
moonsList = []

cursor.execute("SELECT * FROM Moons WHERE NAME = 'The Moon'")
mooninfo = cursor.fetchone()
Moon = moons(mooninfo[0], mooninfo[1], mooninfo[2], mooninfo[3], mooninfo[4], mooninfo[5])
moonsList.append(Moon)

cursor.execute("SELECT * FROM Moons WHERE NAME = 'Titan'")  # (query) tells the db to search the MOONS table for the row where the NAME column is 'Titan' and return all columns of that row
mooninfo = cursor.fetchone()   # (fetchone) retrieves the first row of the result of the query and stores it in the variable titaninfo as a tuple [tuple =list]
Titan = moons(mooninfo[0], mooninfo[1], mooninfo[2], mooninfo[3], mooninfo[4], mooninfo[5])   # creates an instance of the Moon class called Titan by passing the values from the titaninfo tuple to the constructor of the Moons class
moonsList.append(Titan)

cursor.execute("SELECT * FROM Moons WHERE NAME = 'Callisto'")
mooninfo = cursor.fetchone()
Callisto = moons(mooninfo[0], mooninfo[1], mooninfo[2], mooninfo[3], mooninfo[4], mooninfo[5])
moonsList.append(Callisto)

cursor.execute("SELECT * FROM Moons WHERE NAME = 'Io'")
mooninfo = cursor.fetchone()
Io = moons(mooninfo[0], mooninfo[1], mooninfo[2], mooninfo[3], mooninfo[4], mooninfo[5])
moonsList.append(Io)

cursor.execute("SELECT * FROM Moons WHERE NAME = 'Europa'")
mooninfo = cursor.fetchone()
Europa = moons(mooninfo[0], mooninfo[1], mooninfo[2], mooninfo[3], mooninfo[4], mooninfo[5])
moonsList.append(Europa)

cursor.execute("SELECT * FROM Moons WHERE NAME = 'Triton'")
mooninfo = cursor.fetchone()
Triton = moons(mooninfo[0], mooninfo[1], mooninfo[2], mooninfo[3], mooninfo[4], mooninfo[5])
moonsList.append(Triton)

cursor.execute("SELECT * FROM Moons WHERE NAME = 'Deimos'")
mooninfo = cursor.fetchone()
Deimos = moons(mooninfo[0], mooninfo[1], mooninfo[2], mooninfo[3], mooninfo[4], mooninfo[5])
moonsList.append(Deimos)

cursor.execute("SELECT * FROM Moons WHERE NAME = 'Titania'")
mooninfo = cursor.fetchone()
Titania = moons(mooninfo[0], mooninfo[1], mooninfo[2], mooninfo[3], mooninfo[4], mooninfo[5])
moonsList.append(Titania)

for item in moonsList:
    print(vars(item))

# *** Pulling data from the DB, adding each plant as an object, and then adding them to a list of planets called planetList[] ***
planetsList = []   # creates an empty list called planetList to store the planet objects

# Mercury 
cursor.execute("SELECT * FROM Planets WHERE NAME = 'Mercury'")
mercuryInfo = cursor.fetchone()
Mercury = planets(mercuryInfo[0], mercuryInfo[1], mercuryInfo[2], mercuryInfo[3], mercuryInfo[4], mercuryInfo[5], mercuryInfo[6], mercuryInfo[7], mercuryInfo[8], mercuryInfo[9])
planetsList.append(Mercury)   # adds the Mercury object to the planetList

# Venus
cursor.execute("SELECT * FROM Planets WHERE NAME = 'Venus'")
VenusInfo = cursor.fetchone()
Venus = planets(VenusInfo[0], VenusInfo[1], VenusInfo[2], VenusInfo[3], VenusInfo[4], VenusInfo[5], VenusInfo[6], VenusInfo[7], VenusInfo[8], VenusInfo[9])
planetsList.append(Venus)   # adds the Venus object to the planetList

# Earth
cursor.execute("SELECT * FROM Planets WHERE NAME = 'Earth'")
EarthInfo = cursor.fetchone()
Earth = planets(EarthInfo[0], EarthInfo[1], EarthInfo[2], EarthInfo[3], EarthInfo[4], EarthInfo[5], EarthInfo[6], EarthInfo[7], EarthInfo[8], EarthInfo[9])
planetsList.append(Earth)   # adds the Earth object to the planetList

# Mars
cursor.execute("SELECT * FROM Planets WHERE NAME = 'Mars'")
MarsInfo = cursor.fetchone()
Mars = planets(MarsInfo[0], MarsInfo[1], MarsInfo[2], MarsInfo[3], MarsInfo[4], MarsInfo[5], MarsInfo[6], MarsInfo[7], MarsInfo[8], MarsInfo[9])
planetsList.append(Mars)   # adds the Mars object to the planetList

# Jupiter
cursor.execute("SELECT * FROM Planets WHERE NAME = 'Jupiter'")
JupiterInfo = cursor.fetchone()
Jupiter = planets(JupiterInfo[0], JupiterInfo[1], JupiterInfo[2], JupiterInfo[3], JupiterInfo[4], JupiterInfo[5], JupiterInfo[6], JupiterInfo[7], JupiterInfo[8], JupiterInfo[9])
planetsList.append(Jupiter)   # adds the Jupiter object to the planetList

# Saturn
cursor.execute("SELECT * FROM Planets WHERE NAME = 'Saturn'")
SaturnInfo = cursor.fetchone()
Saturn = planets(SaturnInfo[0], SaturnInfo[1], SaturnInfo[2], SaturnInfo[3], SaturnInfo[4], SaturnInfo[5], SaturnInfo[6], SaturnInfo[7], SaturnInfo[8], SaturnInfo[9])
planetsList.append(Saturn)   # adds the Saturn object to the planetList

# Uranus
cursor.execute("SELECT * FROM Planets WHERE Name = 'Uranus'")
UranusInfo = cursor.fetchone()
Uranus = planets(UranusInfo[0], UranusInfo[1], UranusInfo[2], UranusInfo[3], UranusInfo[4], UranusInfo[5], UranusInfo[6], UranusInfo[7], UranusInfo[8], UranusInfo[9])
planetsList.append(Uranus)

# Neptune
cursor.execute("SELECT * FROM Planets WHERE Name = 'Neptune'")
NeptuneInfo = cursor.fetchone()
Neptune = planets(NeptuneInfo[0], NeptuneInfo[1], NeptuneInfo[2], NeptuneInfo[3], NeptuneInfo[4], NeptuneInfo[5], NeptuneInfo[6], NeptuneInfo[7], NeptuneInfo[8], NeptuneInfo[9])
planetsList.append(Neptune)

# Pluto
cursor.execute("SELECT * FROM Planets WHERE Name = 'Pluto'")
PlutoInfo = cursor.fetchone()
Pluto = planets(PlutoInfo[0], PlutoInfo[1], PlutoInfo[2], PlutoInfo[3], PlutoInfo[4], PlutoInfo[5], PlutoInfo[6], PlutoInfo[7], PlutoInfo[8], PlutoInfo[9])
planetsList.append(Pluto)

# for testing: prints all the data in the list: planetsList
for item in planetsList:
    print(vars(item))