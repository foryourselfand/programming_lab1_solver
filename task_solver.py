from abc import ABC, abstractmethod
from typing import List, Union
import re
from task_inputs import TaskInputsCreator
from variant_getter import VariantGetter
from tabs_formatters import *
from os import path, makedirs


class TaskWriter:
    def write_task(self, task_inputs: List[str], variant):
        public_class_main = ClassicFormatter('public class Main')

        psvm = ClassicFormatter('public static void main(String[] args)')
        public_class_main.add(psvm)

        task_formatters = [FirstTaskFormatter(), SecondTaskFormatter(), ThirdTaskFormatter()]
        for task_formatter, task_input in zip(task_formatters, task_inputs):
            task_formatter.format_task(task_input, psvm)
            psvm.add('', end='')

        result = public_class_main.get_result()

        base_dir = f'tasks/{variant}'
        if not path.exists(base_dir):
            makedirs(base_dir)

        file_name = f'{base_dir}/Main.java'
        with open(file_name, 'w') as file:
            file.writelines(result)


class AbstractTaskFormatter(ABC):
    @abstractmethod
    def format_task(self, inputs: str, block: TabFormatter):
        pass

    def arr_creation_left_part(self, arr_type: str, arr_name: str, *arr_sizes: int) -> str:
        brackets = '[]' * len(arr_sizes)
        left_part = f'{arr_type}{brackets} {arr_name}'
        return left_part

    def arr_creation_right_part(self, arr_type: str, arr_name: str, *arr_sizes: int) -> str:
        brackets: str = ''
        for size in arr_sizes:
            brackets += f'[{size}]'
        right_part = f'new {arr_type}{brackets}'
        return right_part

    def arr_creation(self, arr_type: str, arr_name: str, *arr_sizes: int) -> str:
        left_part = self.arr_creation_left_part(arr_type, arr_name, *arr_sizes)
        right_part = self.arr_creation_right_part(arr_type, arr_name, *arr_sizes)
        result = f'{left_part} = {right_part};'
        return result


class FirstTaskFormatter(AbstractTaskFormatter):
    def format_task(self, inputs, block):
        split_input = inputs.split(' ')
        print("inputs:", inputs)
        print("split_input:", split_input)
        print()

        arr_name = split_input[3]
        arr_type = split_input[5][:-1]
        print("arr_name:", arr_name)
        print("arr_type:", arr_type)
        print()

        even_flag = 'чётными' in split_input
        odd_flag = 'нечётными' in split_input
        print('even_flag:', even_flag)
        print('odd_flag:', odd_flag)
        print()

        start_number, end_number = map(int, re.findall(r'\d+', inputs))
        print('start_number:', start_number)
        print('end_number:', end_number)
        print()

        order = split_input[-1][:-1]
        print('order:', order)

        left_part = self.arr_creation_left_part(arr_type, arr_name, 1)
        right_part = self.arr_raw_fill(start_number, end_number, False, False, order)
        full_part = f'{left_part} = {right_part}'
        print('full_part:', full_part)

        block.add(full_part)

    def arr_raw_fill(self, start_number: int, end_number: int, even_flag: bool, odd_flag: bool, order: str) -> str:
        step = 1
        if even_flag or odd_flag:
            step = 2

            mod = 0 if even_flag else 1
            start_number += abs(mod - (start_number % 2))
            end_number -= abs(mod - (end_number % 2))

        arr = [str(elem) for elem in range(start_number, end_number + 1, step)]

        if order == 'убывания':
            arr = arr[::-1]

        numbers_with_dot = ', '.join(arr)
        numbers_in_brackets = '{' + numbers_with_dot + '}'
        return numbers_in_brackets


class SecondTaskFormatter(AbstractTaskFormatter):
    def format_task(self, inputs, block):
        block.add('double[] x = new double[20]')
        second_for = ShortFormatter('for (int i = 0; i < x.length; i++)')
        second_for.add('x[i] = Math.random() * 16.0 - 12.0')
        block.add(second_for)


class ThirdTaskFormatter(AbstractTaskFormatter):
    def format_task(self, inputs, block):
        block.add('double[][] d = new double[14][20]')
        third_for_outer = ClassicFormatter('for (int i = 0; i < d.length; i++)')
        third_for_inner = ClassicFormatter('for (int j = 0; j < d[i].length; j++)')
        third_for_outer.add(third_for_inner)
        block.add(third_for_outer)

        switch = ClassicFormatter('switch ((int) b[i])')
        third_for_inner.add(switch)

        first_case = CaseFormatter('case 7')
        first_case.add('d[i][j] = Math.asin(Math.pow(Math.E, Math.cbrt(- Math.pow(Math.sin(x[j]), 2))))')
        switch.add(first_case)

        for number in [5, 6, 8, 9, 15, 16]:
            switch.add(f'case {number}', end=':')

        second_case = CaseFormatter('case 17')
        second_case.add('d[i][j] = Math.sin(Math.pow(3 * (Math.cos(x[j]) - 1), Math.pow(3 * x[j], 3)))')
        switch.add(second_case)

        default_case = CaseFormatter('default')
        default_case.add('d[i][j] = Math.pow(Math.E, Math.pow(Math.E, 4 * ((1 / 2) + x[j])))')
        switch.add(default_case)

        third_for_inner.add('System.out.printf("%.3f ", d[i][j])')

        third_for_outer.add('System.out.println()')


def main():
    variant = 698

    variant_getter = VariantGetter()

    task_inputs_creator = TaskInputsCreator(variant_getter)
    input_tasks = task_inputs_creator.get_task_inputs(variant)

    task_writer = TaskWriter()
    task_writer.write_task(input_tasks, variant)

    variant_getter.dump_remembered_variants()


if __name__ == '__main__':
    main()
