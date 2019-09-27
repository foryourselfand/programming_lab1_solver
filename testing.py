from pprint import pprint
from bs4 import BeautifulSoup
from typing import Tuple
import requests
from sys import argv


def get_config_info() -> Tuple[str, str]:
    with open("info/config.txt") as file:
        first_param: str = file.readline().replace('\n', '').split(': ')[1]
        second_param: str = file.readline().split(': ')[1]
        return first_param, second_param


def get_soup(config_info: Tuple[str, str]):
    cookies = {
        'JSESSIONID': config_info[0],
        'COOKIE_SUPPORT': 'false',
        'GUEST_LANGUAGE_ID': 'ru_RU'
    }

    params = (
        ('p_auth', config_info[1]),
        ('p_p_id', 'pbportletlab0_WAR_pbportlet'),
        ('p_p_lifecycle', '1'),
        ('p_p_state', 'normal'),
        ('_pbportletlab0_WAR_pbportlet_javax.portlet.action', 'generate'),
    )

    var = argv[1] if len(argv) == 2 else '1'

    data = {
        'var': var
    }

    response = requests.post('https://se.ifmo.ru/courses/programming', params=params, cookies=cookies, data=data)
    page = response.content
    print(type(page))
    soup = BeautifulSoup(page, "html.parser", from_encoding='utf-8')

    return soup


def main():
    config_info: Tuple[str, str] = get_config_info()
    soup: BeautifulSoup = get_soup(config_info)
    print(soup.prettify())
    print('-' * 50)
    first_task = soup.find('li')
    print(first_task.text.split('\n')[0])

    second_task = first_task.find('li')
    print(second_task.text.split('\n')[0])

    third_task = second_task.find('li')
    print(third_task.text.split('\n')[0])

    all_ids = third_task.find_all('li')

    first_if = all_ids[0]
    second_if = all_ids[1]
    third_if = all_ids[2]

    print(first_if.text.split('\n')[0])
    print(second_if.text.split('\n')[0])
    print(third_if.text.split('\n')[0])

    # format_task = third_task.find_all('li')[-1]
    # print(format_task.text.split('\n')[0])


if __name__ == '__main__':
    main()
