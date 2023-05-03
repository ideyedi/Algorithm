#! python
import requests
import datetime


#
# Complete the 'numDevices' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING statusQuery
#  2. INTEGER threshold
#  3. STRING dateStr
#
# https://jsonmock.hackerrank.com/api/iot_devices/search?status=<statusQuery>&page=<pageNumber>
#

def numDevices(statusQuery, threshold, dateStr) -> int:
    # print(statusQuery, threshold, dateStr)
    api_fqdn = "https://jsonmock.hackerrank.com/api/iot_devices/"
    devices = 0

    with requests.session() as s:
        ret = s.get(api_fqdn + "search?status=" + statusQuery)

    total_pages = int(ret.json().get('total_pages'))

    for page in range(1, total_pages + 1):
        with requests.session() as s:
            ret = s.get(api_fqdn + "search?status=" + statusQuery + "&page=" + str(page))

        for data in ret.json().get('data'):
            timestamp = data.get('timestamp')
            root_threshold = data.get('operatingParams').get('rootThreshold')

            timestamp = datetime.datetime.fromtimestamp(timestamp / 1000.0).strftime("%m-%Y")
            # print(timestamp, root_threshold)

            if root_threshold > threshold and timestamp == dateStr:
                devices += 1

    return devices