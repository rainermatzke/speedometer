import datetime
import json
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

print(json.dumps(entry, indent=4))
logfile = str(dt.year) + str(dt.month) + '.log'
print (logfile)