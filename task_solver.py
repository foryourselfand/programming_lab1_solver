from abc import ABC, abstractmethod
from typing import List


class TaskWriter:
    def __init__(self, task_inputs: List[str]):
        self.basic = """public class Main {
    public static void main(String[] args) {
%s
    }
}"""
        addition_formatter = AdditionsFormatter()
        self.addition = addition_formatter.get_addition(task_inputs)

    def write_task(self):
        final = self.basic % self.addition
        print(final)
        with open('tasks/test.java', 'w') as file:
            file.write(final)


class AdditionsFormatter:
    def get_addition(self, task_inputs: List[str]):
        additions: List[str] = list()

        task_formatters = [FirstTaskFormatter(), SecondTaskFormatter(), ThirdTaskFormatter()]

        for task_formatter, task_input in zip(task_formatters, task_inputs):
            raw_formatted_task = task_formatter.get_formatted_task(task_input)
            tab_formatted_task = list()

            for raw_line in raw_formatted_task.split('\n'):
                tab_line = f'\t\t{raw_line}'
                tab_formatted_task.append(tab_line)

            formatted_task = '\n'.join(tab_formatted_task)
            additions.append(formatted_task)

        addition_str = '\n\n'.join(additions)
        return addition_str


class AbstractTaskFormatter(ABC):
    @abstractmethod
    def get_formatted_task(self, inputs) -> str:
        pass


class FirstTaskFormatter(AbstractTaskFormatter):
    def get_formatted_task(self, inputs) -> str:
        return '11\n12'


class SecondTaskFormatter(AbstractTaskFormatter):
    def get_formatted_task(self, inputs) -> str:
        return '21\n22'


class ThirdTaskFormatter(AbstractTaskFormatter):
    def get_formatted_task(self, inputs) -> str:
        return '31\n32'


def main():
    inputs = [str(i) for i in range(3)]
    task_writer = TaskWriter(inputs)
    task_writer.write_task()


if __name__ == '__main__':
    main()
