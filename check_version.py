import requests
import os
import webbrowser

version = str(0) # CHANGE WITH YOUR OWN VERSION THAT MATCH WITH THE PASTEBIN !
check_version = requests.get('#YOUR_PASTEBIN_RAW_LINK')
cv_text = check_version.text

if version == cv_text:
    print("No update available.")
else:
    print("Update available.")
    webbrowser.open_new_tab("") # Here the program will open a new browser tab with the link you add.
    print("Update installed.")

print("Done!")
