import datetime
import json
import os
import pytz
import speedtest

tz = pytz.timezone('Europe/Berlin')
today = datetime.datetime.today()
dt = datetime.datetime(year=today.year, month=today.month, day=today.day,
                       hour=today.hour, minute=today.minute, second=today.second)
timestamp = str(tz.localize(dt))

s = speedtest.Speedtest()
s.get_servers([])
s.get_best_server()
s.download(threads=None)
s.upload(threads=None)
res = s.results.dict()

entry = {
    'timestamp': timestamp,
    'year': dt.year,
    'month': dt.month,
    'protocol': res,
}

logfile = '/home/pi/logs/' + str(dt.year) + str(dt.month) + '.log'
if (os.path.exists(logfile)):
	mode = 'a'
else:
	mode = 'w'
with open(logfile, mode) as myfile:
    myfile.write(json.dumps(entry, indent=4))
    myfile.write(',\n')

