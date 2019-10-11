from abc import ABC, abstractmethod
from typing import List, Union
import re
from task_inputs import TaskInputsCreator
from variant_getter import VariantGetter
from tabs_formatters import *


class TaskWriter:
    def write_task(self, inputs: List[str], variant):
        public_class_main = ClassicFormatter('public class Main')

        psvm = ClassicFormatter('public static void main(String[] args)')

        with open(f'tasks/{variant}.java', 'w') as file:
            file.write(result_str)


class AbstractTaskFormatter(ABC):
    @abstractmethod
    def get_formatted_task(self, inputs) -> str:
        pass


class FirstTaskFormatter(AbstractTaskFormatter):
    def get_formatted_task(self, inputs) -> str:
        print(inputs)

        split_input = inputs.split(' ')
        print(split_input)

        arr_name = split_input[3]
        arr_type = split_input[5][:-1]
        print(arr_name, arr_type)

        even_flag = 'чётными' in split_input
        odd_flag = 'нечётными' in split_input
        print(even_flag, odd_flag)

        numbers = re.findall(r'\d+', inputs)
        print(*numbers)

        order = split_input[-1][:-1]
        print(order)

        arr_size = 10
        array_creation = self.create_array(arr_type, arr_name, arr_size)
        print(array_creation)

        return '11\n12'

    def create_array(self, arr_type: str, arr_name: str, arr_size: Union[int, List[int]]) -> str:
        if type(arr_size) == int:
            arr_size = [arr_size]
        first_brackets = '[]' * len(arr_size)
        first_part = f'{arr_type}{first_brackets} {arr_name}'

        second_brackets: str = ''
        for size in arr_size:
            second_brackets += f'[{size}]'
        second_part = f'new {arr_type}{second_brackets}'

        result = f'{first_part} = {second_part};'
        return result


class SecondTaskFormatter(AbstractTaskFormatter):
    def get_formatted_task(self, inputs) -> str:
        return '21\n22'


class ThirdTaskFormatter(AbstractTaskFormatter):
    def get_formatted_task(self, inputs) -> str:
        return '31\n32'


def main():
    variant = 4

    variant_getter = VariantGetter()

    task_inputs_creator = TaskInputsCreator(variant_getter)
    input_tasks = task_inputs_creator.get_task_inputs(variant)

    task_writer = TaskWriter(input_tasks)
    # task_writer.write_task(variant)

    variant_getter.dump_remembered_variants()


if __name__ == '__main__':
    main()
