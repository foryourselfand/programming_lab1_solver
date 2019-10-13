from solvers.abstract_solver import AbstractTaskSolver
from tabs_formatter import ShortFormatter


class SecondTaskSolver(AbstractTaskSolver):
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
