import httplib2
from apiclient import discovery

import datetime

import quickstart

def main():
    credentials = quickstart.get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    getEventsOfTheDay('markus.oelhafen@sinnerschrader.com', service)

def getEventsOfTheDay(calId, service):
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' idicates UTC time
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    tomorrow = '2017-04-20T00:00:00Z'
    print(now)
    print(tomorrow)
    eventsResult = service.events().list(
        calendarId=calId, timeMin=now, timeMax=tomorrow, singleEvents=True, orderBy='startTime').execute()
    events = eventsResult.get('items', [])
    for event in events:
        print(event['summary'])

def getUpcomingEvents(resultCount):
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' idicates UTC time

    print('Getting the upcoming 10 events')
    eventsResult = service.events().list(
        calendarId='primary', timeMin=now, maxResults=resultCount, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])

def getCalendars(service):
    listResult = service.calendarList().list(pageToken=None).execute()
    lists = listResult.get('items', [])
    print(lists)

if __name__ == '__main__':
    main()
