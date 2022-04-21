from calendar import calendar
import os
from pprint import pprint
from google import Create_Service

CLIENT_SECRET_FILE = 'client_secret_GoogleCloudDemo.json'
API_NAME= 'calendar'
API_VERSION = 'V3'
SCOPES = ['https://www.googleapis.com/auth/calendar.events']

service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

request_body = {
    'summary': 'San Francisco Events'
}

# response = service.calendar().insert(body=request_body)
# print(response)

"""
To delete a calendar
"""

service.calendars().delete(calendarId='56009441415-opsl8c005au9igrv33h8hsjp15n0k65d.apps.googleusercontent.com').excute()