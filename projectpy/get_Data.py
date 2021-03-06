import json
import re
import sys

import requests as r
from bs4 import BeautifulSoup

regex_rm_tags = r"<[^>]*>"
regex_get_links = r"(?:(?:https?|ftp|file):\/\/|www\.|ftp\.)(?:\([-A-Z0-9+&@#\/%=~_|$?!:,.]*\)|[-A-Z0-9+&@#\/%=~_|$?!:,.])*(?:\([-A-Z0-9+&@#\/%=~_|$?!:,.]*\)|[A-Z0-9+&@#\/%=~_|$])"
base_url = "https://shields.io/category/{}"
selectors = {
    'name': '#app > div > div > table > tbody > tr:nth-child({}) > th',
    'link': '#app > div > div > table > tbody > tr:nth-child({}) > td:nth-child(3) > code'
}
lis = ['build', 'codecov', 'analysis', 'chat', 'dependencies', 'size', 'downloads', 'funding',
       'issues', 'license', 'rating', 'social', 'version', 'platform', 'monitoring', 'activity', 'other']


data = {
    'build': {
        'type': [],
    },
    'codecov': {
        'type': [],
    },
    'analysis': {
        'type': [],
    },
    'chat': {
        'type': [],
    },
    'dependencies': {
        'type': [],
    },
    'size': {
        'type': [],
    },
    'downloads': {
        'type': [],
    },
    'funding': {
        'type': [],
    },
    'issues': {
        'type': [],
    },
    'license': {
        'type': [],
    },
    'rating': {
        'type': [],
    },
    'social': {
        'type': [],
    },
    'version': {
        'type': [],
    },
    'platform': {
        'type': [],
    },
    'monitoring': {
        'type': [],
    },
    'activity': {
        'type': [],
    },
    'other': {
        'type': [],
    }
}

for count, item in enumerate(lis[:]):
    resp = r.get(base_url.format(item))
    sys.stdout.write('\r Processing ({}/{}) : {}'.format(count +
                                                         1, len(lis), base_url.format(item)))
    soup = BeautifulSoup(resp.text, 'lxml')
    shield_number = 1
    while shield_number:
        name = soup.select(selectors['name'].format(shield_number))
        link = soup.select(selectors['link'].format(shield_number))
        if name == []:
            pass
        else:
            name = re.sub(regex_rm_tags, ' ', str(
                name[0])).lower().replace(' ', '-')[1:-3]
            data[item]['type'].append({
                # 'name': re.sub(regex_rm_tags, ' ', str(name[0])).lower().replace(' ', '-')[1:-3],
                f"{name}": 'https://img.shields.io' + re.sub(regex_rm_tags, ' ', str(link[0]))[1:-1]
            })
        shield_number += 1
        if shield_number == 59:
            break

    # data = json.dumps(data)
    with open('data.json', 'w') as fp:
        json.dump(data, fp)
