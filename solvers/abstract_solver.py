from abc import ABC, abstractmethod

from tabs_formatter import TabFormatter


class AbstractTaskSolver(ABC):
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
