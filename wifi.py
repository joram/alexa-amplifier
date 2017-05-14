import json
import datetime
import os
import requests
from pyunifi.controller import Controller

def controller():
  host = os.environ.get("UNIFI_URL")
  user = os.environ.get("UNIFI_USER")
  password = os.environ.get("UNIFI_PASSWORD")
  c = Controller(host,user,password,8443,"v5", ssl_verify=False)
  return c

def people_online():
  f = open("people.json")
  all_people = json.load(f)
  online_people = []
  c = controller()
  for person in all_people:
    for mac in person['mac_addresses']:
      client = c.get_client(mac)
      last_seen = client['last_seen']
      dt = datetime.datetime.fromtimestamp(int(last_seen))
      if datetime.datetime.now() - dt < datetime.timedelta(minutes=1):
        online_people.append(person['name'])
  return online_people

