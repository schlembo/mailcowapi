#!/usr/bin/env python

hostAdress = ""
apiKey = "n"
domain = ""
quota = ""

import sys
import requests
import json

action = sys.argv[1]

def insertUser(username, domain, fullname, password, quota):
  connectionString = hostAdress + "/api/v1/add/mailbox"
  attr = {
    "local_part": username,
    "domain": domain,
    "name": fullname,
    "quota": quota,
    "password": password,
    "password2": password,
    "active":"1"
  }
  r = requests.post(connectionString, data={'attr': json.dumps(attr)}, headers={"X-API-Key": apiKey})

def deleteUser(mail):
  connectionString = hostAdress + "/api/v1/delete/mailbox"
  str = '["' + mail + '"]'
  r = requests.post(connectionString, data={'items': str}, headers={"X-API-Key": apiKey})

def changePassword(mail, newPassword):
  connectionString = hostAdress + "/api/v1/edit/mailbox"
  str = '["' + mail + '"]'
  attr = {
    "password": newPassword,
    "password2": newPassword
  }
  r = requests.post(connectionString, data={'items': str, 'attr': json.dumps(attr)}, headers={"X-API-Key": apiKey})

def activateUser(mail):
  connectionString = hostAdress + "/api/v1/edit/mailbox"
  str = '["' + mail + '"]'
  attr = {
    "active":"1"
  }
  r = requests.post(connectionString, data={'items': str, 'attr': json.dumps(attr)}, headers={"X-API-Key": apiKey})

def deactivateUser(mail):
  connectionString = hostAdress + "/api/v1/edit/mailbox"
  str = '["' + mail + '"]'
  attr = {
    "active":"0"
  }
  r = requests.post(connectionString, data={'items': str, 'attr': json.dumps(attr)}, headers={"X-API-Key": apiKey})

if sys.argv[1] == "add":
  if len(sys.argv) == 5:
    insertUser(sys.argv[2], domain, sys.argv[3], sys.argv[4], quota)
  else:
    print("Ungueltige Parameter...")
    print("Parameter fuer diese Aktion sind: username fullname passwort")
elif sys.argv[1] == "changePassword":
  if len(sys.argv) == 4:
    changePassword(sys.argv[2], sys.argv[3])
  else:
    print("Ungueltige Parameter...")
    print("Parameter fuer diese Aktion sind: adresse neuesPasswort")
elif sys.argv[1] == "deactivate":
  if len(sys.argv) == 3:
    deactivateUser(sys.argv[2])
  else:
    print("Ungueltige Parameter...")
    print("Parameter fuer diese Aktion sind: adresse")
elif sys.argv[1] == "activate":
  if len(sys.argv) == 3:
    activateUser(sys.argv[2])
  else:
    print("Ungueltige Parameter...")
    print("Parameter fuer diese Aktion sind: adresse")
elif sys.argv[1] == "delete":
  if len(sys.argv) == 3:
    deleteUser(sys.argv[2])
  else:
    print("Ungueltige Parameter...")
    print("Parameter fuer diese Aktion sind: adresse")
else:
  print("Ungueltige Aktion...")
  print("Gueltige Aktionen sind: add changePassword deactivate activate delete")
