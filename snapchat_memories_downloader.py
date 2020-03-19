import os
import time
import datetime
import json
import urllib
import dateutil.parser
import urlparse
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-f", "--file", dest="file",
                    help="memories_history.json file", metavar="FILE")
json_path = parser.parse_args().file

download_dir = 'memories'

with open(json_path) as f:
    data = json.load(f)

length = len(data['Saved Media'])
index = 1

if not os.path.exists(download_dir):
    os.makedirs(download_dir)

for key in data['Saved Media']:
    print("Dowloading {0}/{1}".format(index, length))

    url = key['Download Link']
    time_stamp = key['Date']
    file_name = urlparse.urlparse(url).path.split("/")[-1]
    file_path = os.path.join(download_dir, file_name)

    if os.path.exists(file_path):
        print('File already exists')
    else:
        urllib.URLopener().retrieve(url, file_path)

    date = dateutil.parser.parse(time_stamp)
    utime = time.mktime(date.timetuple())
    os.utime(file_path, (utime, utime))

    index = index + 1
