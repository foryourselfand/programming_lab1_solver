from abc import ABC, abstractmethod
from pprint import pprint
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

    def arr_creation(self, arr_type: str, arr_name: str, *arr_sizes: str) -> str:
        left_part = self.arr_creation_left_part(arr_type, arr_name, *arr_sizes)
        right_part = self.arr_creation_right_part(arr_type, arr_name, *arr_sizes)
        result = f'{left_part} = {right_part}'
        return result

    def cycle_creation(self, arr_name: str, iter_name: str = 'i'):
        return 'for (int {iter_name} = 0; {iter_name} < {arr_name}.length; {iter_name}++)'.format(iter_name=iter_name,
                                                                                                  arr_name=arr_name)


class FirstTaskFormatter(AbstractTaskFormatter):
    def format_task(self, inputs, block):
        split_input = inputs.split(' ')

        arr_name = split_input[3]
        arr_type = split_input[5][:-1]

        even_flag = 'чётными' in split_input
        odd_flag = 'нечётными' in split_input

        start_number, end_number = map(int, re.findall(r'\d+', inputs))

        order = split_input[-1][:-1]

        left_part = self.arr_creation_left_part(arr_type, arr_name, 1)
        right_part = self.arr_raw_fill(start_number, end_number, even_flag, odd_flag, order)
        full_part = f'{left_part} = {right_part}'

        block.add(full_part)
        block.add('', end='')

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
        split_input = inputs.split(' ')

        arr_name = split_input[3]
        arr_type = split_input[5][:-1]

        arr_size = split_input[8][:-2]

        start_number = float(split_input[-3][1:])
        end_number = float(split_input[-1][:-1])

        array_creation = self.arr_creation(arr_type, arr_name, arr_size)

        cycle_creation = self.cycle_creation(arr_name)

        random_value = self.get_random_value(start_number, end_number)

        random_value_with_right_cast = self.get_random_value_with_right_cast(arr_type, random_value)

        random_arr_filling = self.get_random_arr_filling(arr_name, random_value_with_right_cast)

        block.add(array_creation)
        for_block = ShortFormatter(cycle_creation)
        for_block.add(random_arr_filling)
        block.add(for_block)
        block.add('', end='')

    def get_random_value(self, start_number, end_number) -> str:
        multiplied = start_number + end_number
        random_value = f'Math.random() * {multiplied} - {start_number}'
        return random_value

    def get_random_value_with_right_cast(self, arr_type: str, random_value: str) -> str:
        left_part = ''
        right_part = ''
        if arr_type != 'double':
            left_part = f'({arr_type}) ('
            right_part = ')'
        result = f'{left_part}{random_value}{right_part}'
        return result

    def get_random_arr_filling(self, arr_name: str, random_value, iter_name: str = 'i'):
        left_part = f'{arr_name}[{iter_name}]'
        result = f'{left_part} = {random_value}'
        return result


class ThirdTaskFormatter(AbstractTaskFormatter):
    def format_task(self, inputs, block):
        inputs_arr = inputs.split('\n')
        # for elem in inputs_arr:
        #     print(elem)

        zero_line = inputs_arr[0]

        split_first_line = zero_line.split(' ')

        arr_name = split_first_line[3]
        arr_type = 'double'

        arr_sizes = split_first_line[5][:-1].split('x')

        created_array = self.arr_creation(arr_type, arr_name, *arr_sizes)
        print('created_array:', created_array)

        outer_cycle = self.cycle_creation(arr_name)
        print('outer_cycle:', outer_cycle)

        arr_name_inner_cycle = f'{arr_name}[i]'
        inner_cycle = self.cycle_creation(arr_name_inner_cycle, 'j')
        print('inner_cycle:', inner_cycle)
        print()

        first_line = inputs_arr[1]
        print('first_line:', first_line)

        first_formula_split = first_line.split('`')

        first_formula_before = first_formula_split[0].split(' ')

        checked_arr_name = first_formula_before[2][0]
        print('checked_arr_name:', checked_arr_name)

        first_checked_value = first_formula_before[4][:-1]
        print('first_checked_value:', first_checked_value)

        first_arr_fill = first_formula_split[1]
        print('first_arr_fill:', first_arr_fill)
        print()

        second_line = inputs_arr[2]
        print('second_line:', second_line)

        second_formula_split = second_line.split('`')

        second_formula_before = second_formula_split[0]

        second_in_brackets = second_formula_before.split('{')[1].split('}')[0]

        numbers_in_brackets = second_in_brackets.split(', ')

        numbers_in_brackets_first = numbers_in_brackets[:-1]
        print('numbers_in_brackets_first:', numbers_in_brackets_first)

        number_in_brackets_last = numbers_in_brackets[-1]
        print('number_in_brackets_last:', number_in_brackets_last)

        second_arr_fill = second_formula_split[1]
        print('second_arr_fill:', second_arr_fill)
        print()

        third_line = inputs_arr[3]
        print('third_line:', third_line)
        third_formula_split = third_line.split('`')
        third_arr_fill = third_formula_split[1]
        print('third_arr_fill:', third_arr_fill)
        print()

        last_line = inputs_arr[4]
        print('last_line:', last_line)
        last_line_split = last_line.split(' ')

        comma_raw_number = last_line_split[8]
        print('comma_raw_number:', comma_raw_number)

        block.add('double[][] d = new double[14][20]')
        third_for_outer = ClassicFormatter('for (int i = 0; i < d.length; i++)')
        third_for_inner = ClassicFormatter('for (int j = 0; j < d[i].length; j++)')
        third_for_outer.add(third_for_inner)
        block.add(third_for_outer)

        switch_block = ClassicFormatter('switch ((int) b[i])')
        third_for_inner.add(switch_block)

        first_case = CaseFormatter('case 7')
        first_case.add('d[i][j] = Math.asin(Math.pow(Math.E, Math.cbrt(- Math.pow(Math.sin(x[j]), 2))))')
        switch_block.add(first_case)

        for number in [5, 6, 8, 9, 15, 16]:
            switch_block.add(f'case {number}', end=':')

        second_case = CaseFormatter('case 17')
        second_case.add('d[i][j] = Math.sin(Math.pow(3 * (Math.cos(x[j]) - 1), Math.pow(3 * x[j], 3)))')
        switch_block.add(second_case)

        default_case = CaseFormatter('default')
        default_case.add('d[i][j] = Math.pow(Math.E, Math.pow(Math.E, 4 * ((1 / 2) + x[j])))')
        switch_block.add(default_case)

        third_for_inner.add('System.out.printf("%.3f ", d[i][j])')

        third_for_outer.add('System.out.println()')


def main():
    variant = 24092000

    variant_getter = VariantGetter()

    task_inputs_creator = TaskInputsCreator(variant_getter)
    input_tasks = task_inputs_creator.get_task_inputs(variant)

    task_writer = TaskWriter()
    task_writer.write_task(input_tasks, variant)

    variant_getter.dump_remembered_variants()


if __name__ == '__main__':
    main()
