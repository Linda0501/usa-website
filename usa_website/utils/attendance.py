import gspread
import httplib2

from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name("usa-website/src/usa_website/utils/creds.json", scope)
# usa-website/src/usa_website/utils/creds.json

http = httplib2.Http()
http = credentials.authorize(http)
credentials.refresh(http)

client = gspread.authorize(credentials)
if credentials.access_token_expired:
    client.login()

client = gspread.authorize(credentials)
sheet = client.open("Sp20_Points_Tracker").sheet1
data = sheet.get_all_records()
#print(data)
sid_col = sheet.find("ID").col


def check_sid_exists(sid):  # check in views.py if student id exits
    print(type(sid))
    for i in data:
        if str(i['ID']) == sid:
            return True

    return False

    """
       sid_lst = sheet.col_values(sid_col)
    print(sid_lst)
    for i in sid_lst:
        if i == str(sid):
            return True
    return False
    """


def get_row(sid):  # assume the row exists
    for i in data:
        if str(i['ID']) == sid:
            return i
    return False


def get_points(sid):  # assume valid sid

    row = get_row(sid)
    if row:
        return row['Total']

    """
    total_col = sheet.find("Total").col
    sid_row = sheet.find(str(sid)).row
    return sheet.cell(sid_row, total_col).value
    """


def get_events(sid):  # assume valid sid

    attended_events = []
    row = get_row(sid)
    if row:
        events_lst = list(row.keys())[2:-1]
        for e in events_lst:
            if row[e] != '' and e != "Name" and e != "Total" and e!= "ID" and e!="Email":
                if e == "Donutbot":
                    attended_events.append(str(row[e]) + " Donutbot(s)")
                else:
                    attended_events.append(e)

    return attended_events


"""
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
"""

# testing
#print(check_sid_exists(3034206348))
#print(get_points(3034206348))
#print(get_events(str(3034206348)))
