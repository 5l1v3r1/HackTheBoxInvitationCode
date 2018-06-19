import requests
import json
import base64
import sys

print ""
print "        ==========================================="
print "        |              HackTheBox.eu              |"
print "        |        Invitation Code Generator        |"
print "        -------------------------------------------"
print "        | Devflix.net              By Eren Arslan |"
print "        ==========================================="
print ""
print "        Veuillez patientez..."
print ""
print "        > Code d'invitation : ",base64.b64decode(requests.post("https://www.hackthebox.eu/api/invite/generate", json={"key": "value"}).json()["data"]["code"])
print ""
################################
# By Eren Arslan | Devflix.net #
################################
