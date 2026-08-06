# Recommended source fixes

This file describes the minimal fixes needed to remove the expected-failure markers.
It is intentionally written as a checklist rather than an automatically applied patch,
because the GUI setup uses many globals and should be moved as one coherent block.

1. Classes_and_Objects/APC_Functions.py
   - Delete the module-level call: showEclipses('February', 5, 2000)
   - Add `return moonInfo` at the end of showMoonInfo().
   - Change the Moon query to match the database's canonical name (`The Moon`) or
     update the database and every caller to consistently use `Moon`.

2. GUI_Stuff/basicGUI.py
   - Move lines that create root/canvas/turtle/menu widgets into main().
   - Replace the bare final mainloop() with root.mainloop().
   - Add: if __name__ == "__main__": main()
   - Remove the nested root.mainloop() from dateSelectionFixed().

3. GUI_Stuff/moonpopupgui.py
   - Move popup/canvas/turtle/button creation into a callable function.
   - Do not create a Toplevel during import.

4. Classes_and_Objects/APC_Classes_Objects.py
   - Prefer a load_bodies(connection) function rather than database queries and
     printing at import time.
