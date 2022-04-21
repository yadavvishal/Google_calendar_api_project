import os
from pprint import pprint
from google import Create_Service

CLIENT_SECRET_FILE = 'client_secret_GoogleCloudDemo.json'
API_NAME= 'calendar'
API_VERSION = 'V3'
SCOPES = ['https://www.googleapis.com/auth/calendar.events']

service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)
print(dir(service))