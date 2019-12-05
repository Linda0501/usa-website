import gspread
import httplib2

from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("usa-website/src/usa_website/utils/creds.json", scope)
http = httplib2.Http()
http = credentials.authorize(http)
credentials.refresh(http)
client = gspread.authorize(credentials)
if credentials.access_token_expired:
    client.login()

sheet = client.open("Member_Points").sheet1
data = sheet.get_all_records()

sid_col = sheet.find("ID").col


def check_sid_exits(sid):  # check in views.py if student id exits
    sid_lst = sheet.col_values(sid_col)
    for i in sid_lst:
        if i == sid:
            return True

    return False


def get_points(sid):  # assume valid sid
    total_col = sheet.find("Total").col
    sid_row = sheet.find(str(sid)).row
    return sheet.cell(sid_row, total_col).value


def get_events(sid):  # assume valid sid
    attended_events = []
    events_name = sheet.row_values(1)[2:-1]
    sid_row = sheet.find(str(sid)).row
    sid_points = sheet.row_values(sid_row)[2:-1]
    for i in range(len(events_name)):
        if sid_points[i] != '':
            if events_name[i] == "Donutbot" and int(sid_points[i]) > 1:
                attended_events.append(sid_points[i] + " " + events_name[i] + "s")
            else:
                attended_events.append(events_name[i])

    return attended_events



# testing
#print(get_points(3031855139))
#print(get_events(3031855139))
