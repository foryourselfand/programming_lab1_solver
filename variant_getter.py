import requests
import pickle
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod
from typing import Tuple, Set, Dict
from pprint import pprint


class AbstractPageGetter(ABC):
    @abstractmethod
    def get_page(self, variant) -> bytes:
        pass


class PickleIO:
    def __init__(self, base_dir_name: str = 'variants', file_format: str = 'pickle'):
        self.base_dir_name: str = base_dir_name
        self.file_format: str = file_format

    def get_full_file_name(self, file_name):
        return f'{self.base_dir_name}/{str(file_name)}.{self.file_format}'

    def load(self, file_name):
        with open(self.get_full_file_name(file_name), 'rb') as file:
            data = pickle.load(file)
        return data

    def dump(self, obj, file_name):
        with open(self.get_full_file_name(file_name), 'wb') as file:
            pickle.dump(obj, file)


class RequestPageGetter(AbstractPageGetter, PickleIO):
    def __init__(self):
        super().__init__()
        self.config_info: Tuple[str, str] = self.get_config_info()

    @staticmethod
    def get_config_info() -> Tuple[str, str]:
        with open("info/config.txt") as file:
            first_param: str = file.readline().replace('\n', '').split(': ')[1]
            second_param: str = file.readline().split(': ')[1]
            return first_param, second_param

    def get_page(self, variant) -> bytes:
        cookies = {
            'JSESSIONID': self.config_info[0],
            'COOKIE_SUPPORT': 'false',
            'GUEST_LANGUAGE_ID': 'ru_RU'
        }

        params = (
            ('p_auth', self.config_info[1]),
            ('p_p_id', 'pbportletlab0_WAR_pbportlet'),
            ('p_p_lifecycle', '1'),
            ('p_p_state', 'normal'),
            ('_pbportletlab0_WAR_pbportlet_javax.portlet.action', 'generate'),
        )

        data = {
            'var': str(variant)
        }

        response = requests.post('https://se.ifmo.ru/courses/programming', params=params, cookies=cookies, data=data)
        page = response.content

        self.dump(page, variant)

        return page


class PicklePageGetter(AbstractPageGetter, PickleIO):
    def get_page(self, variant) -> bytes:
        page = self.load(variant)
        return page


class VariantGetter(PickleIO):
    def __init__(self):
        super().__init__('info')
        self.remembered_variants: Set[int] = self.load_remembered_variants()
        self.page_getters: Dict[int, AbstractPageGetter] = {False: RequestPageGetter(),
                                                            True: PicklePageGetter()}

    def load_remembered_variants(self) -> Set[int]:
        data = self.load('remembered_variants')
        return data

    def get_variant_soup(self, variant: int = 698) -> BeautifulSoup:
        page_getter: AbstractPageGetter = self.page_getters[variant in self.remembered_variants]
        self.remembered_variants.add(variant)

        page = page_getter.get_page(variant)
        soup = BeautifulSoup(page, "html.parser", from_encoding='utf-8')

        return soup

    def dump_remembered_variants(self):
        self.dump(self.remembered_variants, 'remembered_variants')


def main():
    variant_getter = VariantGetter()

    soup: BeautifulSoup = variant_getter.get_variant_soup()
    print(soup.prettify())

    variant_getter.dump_remembered_variants()


if __name__ == '__main__':
    main()
