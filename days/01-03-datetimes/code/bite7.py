'''Extract datetimes from log entries and calculate the time
   between the first and last shutdown events'''
from datetime import datetime
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()


def convert_to_datetime(line):
    timestring = line.split()[1]
    dt = (datetime.strptime(timestring, "%Y-%m-%dT%H:%M:%S"))
    return(dt)
    '''TODO 1:
       Given a log line extract its timestamp and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)'''
    pass


def time_between_shutdowns(loglines):
    shutdowntimes = []
    for line in loglines:
        if SHUTDOWN_EVENT in line:
            dt = convert_to_datetime(line)
            shutdowntimes.append(dt)
    if len(shutdowntimes) > 0:
        shutdown_delta = max(shutdowntimes) - min(shutdowntimes)
        return(shutdown_delta)
    '''TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and calculate the
       timedelta between the first and last one.
       Return this datetime.timedelta object.'''
    pass


tbs = time_between_shutdowns(loglines)
print('Time between shutdowns = ' + str(tbs))
