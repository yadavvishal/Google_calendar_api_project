import os
from pprint import pprint
from Google import Create_Service

CLIENT_SECRET_FILE = 'client_secret_GoogleCloudDemo.json'
API_NAME= 'calendar'
API_VERSION = 'V3'
SCOPES = ['https://www.googleapis.com/auth/calendar.events']

service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)
response = service.calendarList().list().execute()
pprint(response)

print(dir(response))