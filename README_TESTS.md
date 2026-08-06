# APC Antikythera unit-test suite

This suite uses Python's built-in `unittest` framework. No additional test framework is required.

## Required case pattern

Every production function or behavior covered by this suite has exactly four top-level test methods:

- `test_common_1_...`
- `test_common_2_...`
- `test_uncommon_1_...`
- `test_uncommon_2_...`

A test method may use `subTest()` to check closely related branches while still remaining one of the four required cases. “Uncommon” means a boundary, missing record, unusual but accepted value, invalid target, or dependency failure.

## Install

Copy these items into the root of the `APC_Antikythera` repository:

- `tests/`
- `run_tests.py`
- `.github/workflows/unit-tests.yml` (optional)

The resulting layout should look like:

```text
APC_Antikythera/
├── Calculation_Stuff/
├── Classes_and_Objects/
├── Database_Stuff/
├── GUI_Stuff/
├── tests/
├── run_tests.py
└── requirements.txt
```

Install dependencies and run from the repository root:

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
```

or:

```bash
python run_tests.py
```

## Coverage

### `Calculation_Stuff/solarfunc.py`

Each of these has two common and two uncommon cases:

- `rect2polar`
- `strip_z`
- `sv_to_coord`
- `daylightSavings`
- `moonphase`
- `moon`
- `planets`
- `sunriseSet`
- `JMoons`
- `Equinox`

### `Calculation_Stuff/solarapi.py`

- `Request.__init__`
- `handle_request`

The four `handle_request` cases use subtests to cover every request type, successful targeted and untargeted lookups, normalization, invalid targets, malformed requests, and dependency failures.

### `Classes_and_Objects/APC_Functions.py`

- `monthConversion`
- `showEclipses`
- `showPlanetInfo`
- `showMoonInfo`
- `showSmallbodies`

### `Classes_and_Objects/APC_Classes_Objects.py`

- `solarBodies.__init__`
- `planets.__init__`
- `moons.__init__`
- `planets.printInfo`
- `moons.printInfo`

### Database and GUI behavior

- database creation and schema
- representative seed data
- idempotent reruns
- preserving existing primary-key rows
- planet movement
- moon movement
- datetime increments
- planet-information formatting
- GUI import safety

## Expected failures

Five tests are marked `expectedFailure`. They document existing defects without failing the complete run:

1. `showMoonInfo()` fetches a row but never returns it.
2. `basicGUI.py` creates `Tk()` during import.
3. `basicGUI.py` calls `mainloop()` during import.
4. `moonpopupgui.py` creates `Toplevel()` during import.
5. `moonpopupgui.py` assigns the popup object during import.

Once a source defect is fixed, remove the corresponding `@unittest.expectedFailure` decorator.

## Unit tests versus manual GUI testing

Tkinter layout appearance, menus, images, and the continuous turtle animation still need a short manual test. The automated GUI tests deliberately load selected definitions through the AST so no real window is opened during the test run.
