# -*- coding: utf-8 -*-
#Get authentication to use google API
import httplib2
import os
import pickle

import gspread
from oauth2client.service_account import ServiceAccountCredentials

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient import discovery

import oauth2client
from oauth2client import file
from oauth2client import client
from oauth2client import tools

import google_auth_oauthlib

#from multiprocessing import Pool
from cachetools import cached, TTLCache
cacheHeaders = TTLCache(maxsize=9, ttl=172800)
cacheSIDs = TTLCache(maxsize=150, ttl=172800)

#Full code takes about 6 seconds TODO: See if we can lower that

try:
    import argparse
    flags = tools.argparser.parse_args([])
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
HOME_DIR = os.path.dirname(os.path.abspath(__file__))
CLIENT_SECRET_LOC = os.path.join(HOME_DIR, 'client_secret.json')
APPLICATION_NAME = 'SusaClient'
REDIRECT_URI = 'http://127.0.0.1:8000/attendance'
#You wouldn't steal a car would you? So please don't steal our credentials! Thanks!

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open("Member_Points").sheet1

member_points_sheet = sheet.get_all_records()
print(member_points_sheet)

def get_credentials():
    # if os.path.dirname(os.path.abspath(__file__)) == '/home/u/ug/ugradsa/usa-website/src/usa_website/utils':
    #     HOME_DIR = '/home/u/ug/ugradsa/usa-website/src/usa_website/utils/'
    # else:
    #HOME_DIR = './usa_website/utils'
    HOME_DIR = os.path.dirname(os.path.abspath(__file__))
    credential_dir = os.path.join(HOME_DIR, '.credentials')
    http = httplib2.Http(cache=".cache")
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'credentials.json')

    store = oauth2client.file.Storage(credential_path)

    credentials = google.oauth2.credentials.Credentials(
    'access_token',
    refresh_token='refresh_token',
    token_uri='token_uri',
    client_id='client_id',
    client_secret='client_secret')

    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_LOC, SCOPES)
        flow.params['access_type'] = 'offline'
        flow.params['approval_prompt'] = 'force'
        flow.params['redirect_uri'] = REDIRECT_URI
        if flags:
            credentials = flow.run_local_server()
        print(credentials)
        print('storing credentials to' + credential_path)
    return credentials

@cached(cacheHeaders)
def GetAttendanceHeader(SID):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = build('sheets', 'v4', http)
    #SPREADSHEET_ID = '1dnLK86wVXIvtJ5sOPUgPKkDRap6IG11q8ZqUXvixmAE'
    SPREADSHEET_ID = '1GKam1J_GWbjy7_W221mbrdUmeDCtW6I5WshxMkvgAWQ'
    range='A1:O1'
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=range).execute()
    values=result.get('values', [])
    flat_values = [item for sublist in values for item in sublist]
    return(flat_values)

@cached(cacheSIDs)
def LookupSIDs():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = build('sheets', 'v4', http)
    SPREADSHEET_ID = '1dnLK86wVXIvtJ5sOPUgPKkDRap6IG11q8ZqUXvixmAE'
    range='C2:C148'
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=range).execute()
    values=result.get('values', [])
    print("lookup called")
    return values

def GetAttendanceDetails(SID, values):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = build('sheets', 'v4', http)
    SPREADSHEET_ID = '1dnLK86wVXIvtJ5sOPUgPKkDRap6IG11q8ZqUXvixmAE'
    icounter = 0
    flat_values = [item for sublist in values for item in sublist]
    for i,val in enumerate(flat_values):
        if SID == val:
            icounter = i + 2 #account for python index starting at 0 and SIDs starting at row 2
    if icounter <= 1:
        return(1)
    else:
        new_range='A'+ str(icounter) + ':O' + str(icounter)
        print(new_range)
        new_result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=new_range).execute()
        new_values=new_result.get('values', [])
        alph = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O']
        new_flat_values = [item for sublist in new_values for item in sublist]
        final_values = [x or '0' for x in new_flat_values]
        i = len(alph) - len(final_values)
        while i > 0:
            final_values.append(0)
            i=i-1
        print(final_values)
        print(new_range)
        print(new_result)
    return(final_values)


""
{
  "type": "service_account",
  "project_id": "attendance-256904",
  "private_key_id": "f314ba2eb9856f04e4919c6d124f35bcae0591c4",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDpbhlDf5q6v0Pr\netk6dicM/D4C6EaUJhuOKS2UYZGqo98Yia0Mq2D+Ib8NWLH1+NZk4L7HDnV3jC4R\nzE12NTHbLfBbWuJ5Agp9SFKX0CvnnJ4v3cDyNLHsPNEPhtQfAl3i5NCrbzEWn/iw\nE5E447cPuD+a5mxjpeIplWJk5ZBX1sSWAuqJlrbElLyNXRxFDBP5RG2lLCpAxgCS\nG8yQvLixFwKpKmZrfxP5oyAwtKschW+mLERS92DAglC8oWo+nXtFhRMIWKIbXzvG\nUrrrBI9O4at5b8cdCoZmnr/eB4aRoFUZ7cGIgo06RYf0mlAUDCftEydRrvX7ydOu\nNtOl1CatAgMBAAECggEAH9ZS3shoJ6FPl63tM9KKl/RNVuMsQSeDaZvHKi42imII\nWxXoAsrbEz4yCxV2TDiQsTiP/KFFtzTo0aeeRwmRT7YPyr32FpAHMzgqf6c2XcQY\nNSoXF1HFlJVk5Cu9Aa+2c2xG46LqPI48AnPgwjQYsy2riypzTRICay6DOYSv77LJ\n6x1xGNKsKpNaDTvvxRATBSKGqXWGGId0q5tg0SD8ReOljtt5pt/+Lb4MyuwheapY\no5jw6iVOhV3WClUOs51RtJAOeiA0Hu/xGtoOCabJKjFFdozP+zlMGM4c2jHNw+1s\nLcjaYsZOxLiQkFu2lj03boo9Jw6CfnF6B/gjK85IoQKBgQD9G2qUOephlWydhJoq\n70TTGLODzsh0JM3G5qr7zKDE3XdEMIM2R361RQc5bBFt7u4nprmwITpNDGMzRcRC\n8aPrsmQG7IlAtH5sR3l7tYqZ7ZyaJs1XoomSiEcCH2DTCC5Rtxqfy5Wl6txu0BL5\naFyMjxv0H2UutjwpFF767Vom8QKBgQDsGRulbAw/ucKd7AV87VxdspGT9dwVmBDg\n9HxqvD0ihyvhvdUZE0V9zU34d/EHT9IvcMY8hjh/NrmH+OMqvzSbkGLuzfYCTFdd\nf9FcFinXy5ki6be+KpNNQGLkW2/tnMz8Uf9rPUGiW7OymU0LCIr/+Pm+UmOf6+Vv\nVOpxvx9TfQKBgQCOrvLxJokDg+ncDpGeXI4O9qDUUDDekJTUaNrA4gVLlZGThkmh\nwsIiTAybiVl2ALiO78VEDidAohgWImFWX8RJraIH6TYinN2cCtroK1o8FiAvImql\n2YH2cg6dmrTJopYCCNfgdzMgenrTmUbpBLUPo+ldQImYwLC/c7VrfXxR8QKBgQCF\n4kcXK4pWqNSAEVObYE68o4KCUS2Y4T7RElNrg4t3hQeRX8D0E0WY7U+F0x5PcyhR\n1rXTpJltKm9TeAP6PatrfBleKlWTQA9a6hyjB756rO4OKlMT97jIWfa6YE+8guqL\nO0SIX5hUpYPlh6F03EdWmK2nC7mK+o6E77ZzAlqVUQKBgFozwH2lJMlVzUuSSsYw\nXptGYyRSiiFUT+ngE+lfjHsVTCdeIIBg5xqiupUlmW4QDaW0MAkQ7UsovujDjz6e\niXUr4xaVHfoLS7nrrQeMAy8+DGpemdDKH6WomFs+xrf17l1vaeN44KrhWi92xqZ8\nZXks8gLBZO5c0f7F0NcQqoS+\n-----END PRIVATE KEY-----\n",
  "client_email": "attendance-points@attendance-256904.iam.gserviceaccount.com",
  "client_id": "115544069776750181243",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/attendance-points%40attendance-256904.iam.gserviceaccount.com"
}
""
