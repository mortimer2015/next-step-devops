import sys
import re
import datetime
import threading
import os

#print(sys.argv[1])

# a = '127.0.0.1 - - [18/Aug/2017:10:39:43 +0800] "POST /jsrpc.php?output=json-rpc HTTP/1.1" 200 65 "http://127.0.0.1/screens.php?ddreset=1" "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"'
#o = re.compile(r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) .* .* \[(?P<time>.*)\] "(?P<method>.*) (?P<url>.*) (?P<version>.*)" (?P<status>\d*) (?P<length>\d*) "(?P<referer>.*)" "(?P<ua>.*)"')
#m = o.search(a.rstrip('\n'))
#d = m.groupdict()
#d['time'] = datetime.datetime.strptime(d['time'], '%d/%b/%Y:%H:%M:%S %z')
#print(d['ip'], d['time'])
#threading.Event(1)

event = threading.Event()

while event.is_set():
    print(1)
    event.wait(2)


def open_log():
    offset = 0
    with open('1') as f:
        f.seek(offset)
        yield from f
        offset = f.tell()
        print(offset)
print(os.stat('1').st_size)


for i in open_log():
    print(i)