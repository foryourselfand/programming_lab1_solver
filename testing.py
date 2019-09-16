from pprint import pprint
from bs4 import BeautifulSoup

import requests

cookies = {
    'JSESSIONID': 'a16a8093b726332ff805e44f5f47',
    'COOKIE_SUPPORT': 'false',
    'GUEST_LANGUAGE_ID': 'ru_RU',
}

params = (
    ('p_auth', '0M9spBX7'),
    ('p_p_id', 'pbportletlab0_WAR_pbportlet'),
    ('p_p_lifecycle', '1'),
    ('p_p_state', 'normal'),
    ('_pbportletlab0_WAR_pbportlet_javax.portlet.action', 'generate'),
)

data = {
    'var': '1'
}

response = requests.post('https://se.ifmo.ru/courses/programming', params=params, cookies=cookies, data=data)
page = response.content
soup = BeautifulSoup(page, "html.parser", from_encoding='utf-8')

print(soup.prettify())
