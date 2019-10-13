from os import path, makedirs

from solvers.first_solver import FirstTaskSolver
from solvers.second_solver import SecondTaskSolver
from solvers.third_solver import ThirdTaskSolver
from tabs_formatter import *


class TaskWriter:
    def write_task(self, task_inputs: List[str], variant, print_flag: bool = False):
        public_class_main = ClassicFormatter('public class Main')

        psvm = ClassicFormatter('public static void main(String[] args)')
        public_class_main.add(psvm)

        task_formatters = [FirstTaskSolver(), SecondTaskSolver(), ThirdTaskSolver()]
        for task_formatter, task_input in zip(task_formatters, task_inputs):
            task_formatter.format_task(task_input, psvm)

        result = public_class_main.get_result()

        if print_flag:
            for line in result:
                print(line, end='')

        base_dir = f'tasks/{variant}'
        if not path.exists(base_dir):
            makedirs(base_dir)

        file_name = f'{base_dir}/Main.java'
        with open(file_name, 'w') as file:
            file.writelines(result)
