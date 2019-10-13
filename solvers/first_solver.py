import re

from solvers.abstract_solver import AbstractTaskSolver


class FirstTaskSolver(AbstractTaskSolver):
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
