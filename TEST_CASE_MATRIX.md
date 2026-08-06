# Test-case matrix

Every row below corresponds to one test class with four methods.

| Test target | Common case 1 | Common case 2 | Uncommon case 1 | Uncommon case 2 |
|---|---|---|---|---|
| `rect2polar` | first quadrant | second quadrant | origin | negative floats |
| `strip_z` | tuple | list | already 2-D | extra dimensions |
| `sv_to_coord` | integer vector | float vector | zero vector | extra fields |
| `daylightSavings` | winter | summer | before DST switch | after DST switch |
| `moonphase` | waxing gibbous | waning crescent | exact half/month rollover | new/full boundaries |
| `moon` | explicit time | default time | negative angle | library exception |
| `planets` | explicit time | default time | empty result | library exception |
| `sunriseSet` | summer | winter | leap day | library exception |
| `JMoons` | explicit time | default time | leap day | time error |
| `Equinox` | current year | another year | year 1 | engine error |
| `Request` | defaults | explicit values | `None` request | independent payloads |
| `handle_request` | scalar endpoints | collections/targets | normalization/404s | malformed/500s |
| `monthConversion` | January | July | wrong case | unknown/empty/None |
| `showEclipses` | solar match | lunar match | no match | invalid month |
| `showPlanetInfo` | Earth | Mars | missing planet | quote/injection-shaped input |
| `showMoonInfo` | Io | Europa | unsupported moon | missing return defect |
| `showSmallbodies` | start month | end month | no result | numeric/stringified input |
| `solarBodies.__init__` | integer fields | float fields | zeros/None | mutable position |
| `planets.__init__` | Earth | gas giant | zeros/None | negative values |
| `moons.__init__` | Earth moon | Io | no parent | negative values |
| `planets.printInfo` | Earth | gas giant | None values | negative values |
| `moons.printInfo` | Earth moon | Io | None values | negative values |
| database builder | file/schema | seed rows | second run | preserve existing row |
| `Planet.move_solarSystem` | 0° | 90° | zero radius | negative radius |
| `Moon.move_moonPlanet` | 0° | 180° | zero radius | negative radius |
| `increment_datetime` | same day | next day | negative hours | leap day/fractional hours |
| `openPlanetWindow` | Earth | Jupiter | missing record | unusual values |
| GUI import safety | no `Tk()` | no `mainloop()` | no `Toplevel()` | no import-time popup assignment |
