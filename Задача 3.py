import requests
from datetime import datetime, timedelta


def get_posts_with_tags():
    diff_days = timedelta(days=2)
    today = datetime.now()
    days_ago = today - diff_days
    today_timestamp = round(today.timestamp())
    days_ago_timestamp = round(days_ago.timestamp())

    url = 'https://api.stackexchange.com/2.3/questions'
    # url = 'http://92.119.90.43:1205'
    params = {'fromdate': days_ago_timestamp, 'todate': today_timestamp, 'order': 'desc', 'sort': 'creation',
              'tagged': 'python', 'site': 'stackoverflow'}
    resp = requests.get(url, params=params)
    return resp, resp.json()

#
# print(get_posts_with_tags())
print(datetime(year=2020, month=5, day=6).timestamp())

