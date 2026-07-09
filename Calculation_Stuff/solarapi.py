import solarfunc as sf

JMOON_NAMES = {
    "io": "io",
    "europa": "europa",
    "ganymede": "ganymede",
    "callisto": "callisto"
}

class Request():
    def __init__(self, REQ, year, month=1, day=1, hour=12, minute=0, target=None):
        self.request = REQ
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.response = 400
        self.payload = []
        self.target = target

def handle_request(req):
    request_type = req.request.lower()
    try:
        if request_type == "moonphase":
            req.payload = sf.moonphase(
                req.year,
                req.month,
                req.day,
                req.hour,
                req.minute
            )

        elif request_type == "moon":
            req.payload = sf.moon(
                req.year,
                req.month,
                req.day,
                req.hour,
                req.minute
            )

        elif request_type == "planets":
            planets = sf.planets(
                req.year,
                req.month,
                req.day,
                req.hour,
                req.minute
            )
            if req.target is not None:
                target = req.target.capitalize()

                if target in planets:
                    req.payload = sf.strip_z(planets[target])
                else:
                    req.response = 404
                    req.error = "Planet not found"
                    return req
            else:
                req.payload = {}
                for name, coord in planets.items():
                    req.payload[name] = sf.strip_z(coord)

        elif request_type == "sunriseset":
            req.payload = sf.sunriseSet(
                req.year,
                req.month,
                req.day
            )

        elif request_type == "jmoons":
            moons = sf.JMoons(
                req.year,
                req.month,
                req.day,
                req.hour,
                req.minute
            )
            if req.target is not None:
                target = req.target.strip().lower()

                if target in JMOON_NAMES:
                    moon_attr = JMOON_NAMES[target]
                    moon_state = getattr(moons, moon_attr)
                    req.payload = sf.sv_to_coord(moon_state)
                else:
                    req.response = 404
                    req.error = "Jupiter moon not found"
                    return req
            else:
                req.payload = {
                    "Io": sf.sv_to_coord(moons.io),
                    "Europa": sf.sv_to_coord(moons.europa),
                    "Ganymede": sf.sv_to_coord(moons.ganymede),
                    "Callisto": sf.sv_to_coord(moons.callisto)
                }

        elif request_type == "equinox":
            sols = sf.Equinox(req.year)
            if req.target is not None:
                match req.target.lower():
                    case "march":
                        req.payload = sols.mar_equinox
                    case "june":
                        req.payload = sols.jun_solstice
                    case "september":
                        req.payload = sols.sep_equinox
                    case "december":
                        req.payload = sols.dec_solstice
                    case _:
                        req.response = 404
                        req.error = "Invalid month"
                        return req
            else:
                req.payload = {
                    "March Equinox": sols.mar_equinox,
                    "June Solstice": sols.jun_solstice,
                    "September Equinox": sols.sep_equinox,
                    "December Solstice": sols.dec_solstice
                }


        else:
            req.response = 404
            req.error = "Unknown request type"
            return req

        req.error = "None"
        req.response = 200
        return req

    except Exception as e:
        req.response = 500
        req.error = str(e)
        req.payload = []
        return req
