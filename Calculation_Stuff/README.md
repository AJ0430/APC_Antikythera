# Solarsystem Calculations

These are the fuctions for various calculations within the solarsystem. The functions can be indirectly accessed by importing the solarapi python file and passing requests to it.

Usage: handle_request(request, year, month=1, day=1, hour=12, minute=0, target=None) \
The only inputs required to successfully pass a request are the request value and the year. The rest defaults to 12pm on January 1st. Note that the target value is for returning specific coordinates or times for the planet coordinates, jupiter moon coordinates, and equinox date and times.

##All coordinate units are in degrees

Valid requests:
"moonphase" -> returns the moon phase and whether it is waxing or waning \
"moon" -> returns the angle for the moon at a given time \
"planets" -> returns the angles of all the planets in the solar system unless a given planet is passed with the target argument \
"sunriseset" -> returns the sunrise and sunset times for a given date \
"jmoons" -> returns the angles of jupiter's moons unless a given moon is passed with the target argument \
"equinox" -> returns the date and times for all of the solstices and equinoxes of a given year \
