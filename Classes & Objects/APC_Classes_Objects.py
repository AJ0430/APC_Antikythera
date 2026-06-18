import sqlite3

# tells the program to connect to the database and creates a cursor to execute commands
conn = sqlite3.connect('Database Stuff/AntikytheraSystem.db')
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