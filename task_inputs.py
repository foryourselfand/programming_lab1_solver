from typing import Union
from bs4 import BeautifulSoup, Tag

from variant_getter import VariantGetter


class TaskInputsCreator:
    def __init__(self, variant_getter):
        self.variant_getter: VariantGetter = variant_getter
        self.last_element: Union[BeautifulSoup, Tag, None] = None

    def get_task_inputs(self, variant: int = 698):
        soup: BeautifulSoup = self.variant_getter.get_variant_soup(variant)
        # print(soup.prettify())
        # print('_' * 100)

        self.last_element = soup
        first_text = self.get_text_from_last_element()
        second_text = self.get_text_from_last_element()

        third_texts = list()
        third_start = self.get_text_from_last_element()
        third_texts.append(third_start)

        all_li = self.last_element.find_all('li')
        for temp_li in all_li:
            temp_text = self.get_text(temp_li)
            third_texts.append(temp_text)
        third_text = '\n'.join(third_texts)

        task_inputs = list()
        task_inputs.append(first_text)
        task_inputs.append(second_text)
        task_inputs.append(third_text)

        return task_inputs

    def get_text_from_last_element(self):
        li = self.last_element.find('li')
        self.last_element = li

        return self.get_text(li)

    @staticmethod
    def get_text(element: Tag):
        return element.text.split('\n')[0]


def main():
    variant_getter = VariantGetter()

    task_inputs_creator = TaskInputsCreator(variant_getter)
    input_tasks = task_inputs_creator.get_task_inputs()
    for input_task in input_tasks:
        print(input_task)
        print()

    variant_getter.dump_remembered_variants()


if __name__ == '__main__':
    main()
