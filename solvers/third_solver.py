from formula_converter import FormulaConverter
from solvers.abstract_solver import AbstractTaskSolver
from tabs_formatter import TabFormatter, ClassicFormatter, CaseFormatter


class ThirdTaskSolver(AbstractTaskSolver):
    def __init__(self):
        self.arr_name = ''
        self.for_outer_block = None
        self.for_inner_block = None
        self.switch_block = None

        self.raw_str_to_number = {'двумя': 2,
                                  'тремя': 3,
                                  'четырьмя': 4,
                                  'пятью': 5}

    def convert_formula(self, full_str: str) -> str:
        equality_split = full_str.split(' = ')

        formula_raw = equality_split[1]
        formula_result = FormulaConverter.convert_formula(formula_raw)

        equality_result = f'{equality_split[0]} = {formula_result}'

        return equality_result

    def format_task(self, inputs, block):
        inputs_arr = inputs.split('\n')

        self.zero_line_handle(inputs_arr, block)

        self.first_line_handle(inputs_arr)

        self.second_line_handle(inputs_arr)

        self.third_line_handle(inputs_arr)

        self.last_line_handle(inputs_arr)

        self.for_outer_block.add('System.out.println()')

    def zero_line_handle(self, inputs_arr, block: TabFormatter):
        zero_line = inputs_arr[0]

        split_first_line = zero_line.split(' ')

        self.arr_name = split_first_line[3]
        arr_type = 'double'

        arr_sizes = split_first_line[5][:-1].split('x')

        created_array = self.arr_creation(arr_type, self.arr_name, *arr_sizes)

        outer_cycle = self.cycle_creation(self.arr_name)

        arr_name_inner_cycle = f'{self.arr_name}[i]'
        inner_cycle = self.cycle_creation(arr_name_inner_cycle, 'j')

        block.add(created_array)
        self.for_outer_block = ClassicFormatter(outer_cycle)
        self.for_inner_block = ClassicFormatter(inner_cycle)
        self.for_outer_block.add(self.for_inner_block)
        block.add(self.for_outer_block)

    def first_line_handle(self, inputs_arr):
        first_line = inputs_arr[1]

        first_formula_split = first_line.split('`')

        first_formula_before = first_formula_split[0].split(' ')

        checked_arr_name = first_formula_before[2][0]
        switch_str = f'switch ((int) {checked_arr_name}[i])'

        first_checked_value = first_formula_before[4][:-1]
        first_case_str = f'case {first_checked_value}'

        first_arr_fill_raw = first_formula_split[1]
        first_arr_fill_result = self.convert_formula(first_arr_fill_raw)

        self.switch_block = ClassicFormatter(switch_str)
        self.for_inner_block.add(self.switch_block)

        first_case = CaseFormatter(first_case_str)
        first_case.add(first_arr_fill_result)
        self.switch_block.add(first_case)

    def second_line_handle(self, inputs_arr):
        second_line = inputs_arr[2]

        second_formula_split = second_line.split('`')

        second_formula_before = second_formula_split[0]

        second_in_brackets = second_formula_before.split('{')[1].split('}')[0]

        numbers_in_brackets = second_in_brackets.split(', ')

        numbers_in_brackets_first = numbers_in_brackets[:-1]

        number_in_brackets_last = numbers_in_brackets[-1]
        second_case_str = f'case {number_in_brackets_last}'

        second_arr_fill_raw = second_formula_split[1]
        second_arr_fill_result = self.convert_formula(second_arr_fill_raw)

        for number in numbers_in_brackets_first:
            self.switch_block.add(f'case {number}', end=':')

        second_case = CaseFormatter(second_case_str)
        second_case.add(second_arr_fill_result)
        self.switch_block.add(second_case)

    def third_line_handle(self, inputs_arr):
        third_line = inputs_arr[3]
        third_formula_split = third_line.split('`')
        third_arr_fill_raw = third_formula_split[1]
        third_arr_fill_result = self.convert_formula(third_arr_fill_raw)

        default_case = CaseFormatter('default')
        default_case.add(third_arr_fill_result)
        self.switch_block.add(default_case)

    def last_line_handle(self, inputs_arr):
        last_line = inputs_arr[4]
        last_line_split = last_line.split(' ')

        comma_raw_number = last_line_split[8]

        real_number = self.raw_str_to_number[comma_raw_number]

        souf_str = f'System.out.printf("%.{real_number}f ", {self.arr_name}[i][j])'

        self.for_inner_block.add(souf_str)
