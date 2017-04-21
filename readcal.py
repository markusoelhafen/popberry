import httplib2
from apiclient import discovery

import datetime
import quickstart

def main():
    credentials = quickstart.get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    calendarIds = ['65lu3jc07jnt7k19tn4466qdbc@group.calendar.google.com', 'primary']

    allEvents = getEventsOfTheDay(calendarIds, service)

    for event in allEvents:
        print(event['summary'], event['start']['dateTime'])

def getEventsOfTheDay(calId, service):
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time #define current time
    tomorrow = (datetime.datetime.utcnow() + datetime.timedelta(days=1)).isoformat() + 'Z' #define current time + 24h

    eventlist = [] #create empty list

    for cal in calId: #iterate through all specified calendarIDs
        eventsResult = service.events().list(calendarId=cal, timeMin=now, timeMax=tomorrow, singleEvents=True, orderBy='startTime').execute() #call google calendar api
        events = eventsResult.get('items', []) #save returned events in variable
        for event in events: # iterate through calendar events
            eventlist.append(event) # append the event to the eventlist list (this is still sorted calendar after calendar)

    eventlist = sorted(eventlist, key=lambda event: event['start']['dateTime']) # sort the eventlist by the start time of an event
    return eventlist

    # return(eventlist)

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
    # print(lists)
    for list in lists:
        print(list['summary'],': ',list['id'])

if __name__ == '__main__':
    main()
