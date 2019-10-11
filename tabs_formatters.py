from abc import abstractmethod
from pprint import pprint


class TabFormatter:
    def __init__(self, header):
        self.lines = []

        self.childs = []
        self.orders = []

        self.final_result = []
        self.final_result.append(f'{header}{self.get_header_start()}\n')

    def add_line(self, line, end=';'):
        self.lines.append(f'\t{line}{end}\n')
        self.orders.append('line')

    def add_child(self, child):
        self.childs.append(child)
        self.orders.append('child')

    def get_result(self):
        line_iter = 0
        child_iter = 0
        for order in self.orders:
            if order == 'line':
                self.final_result.append(self.lines[line_iter])
                line_iter += 1
            elif order == 'child':
                child_results = self.childs[child_iter].get_result()
                for child_result in child_results:
                    self.final_result.append(f'\t{child_result}')
                child_iter += 1
        self.final_result.append(f'{self.get_header_end()}\n')
        return self.final_result

    @abstractmethod
    def get_header_start(self) -> str:
        pass

    @abstractmethod
    def get_header_end(self) -> str:
        pass


class ClassicFormatter(TabFormatter):
    def get_header_start(self) -> str:
        return ' {'

    def get_header_end(self) -> str:
        return '}'


class ShortFormatter(TabFormatter):
    def get_header_start(self) -> str:
        return ''

    def get_header_end(self) -> str:
        return ''


class CaseFormatter(TabFormatter):
    def get_header_start(self) -> str:
        return ':'

    def get_header_end(self) -> str:
        return '\tbreak;'


if __name__ == '__main__':
    public_class_main = ClassicFormatter('public class Main')

    psvm = ClassicFormatter('public static void main(String[] args)')
    psvm.add_line('short[] b = new short[14]')
    public_class_main.add_child(psvm)

    first_for = ShortFormatter('for (short i = 0, j = 18; i < b.length; i++, j--)')
    first_for.add_line('b[i] = j')
    psvm.add_child(first_for)

    psvm.add_line('double[] x = new double[20]')
    second_for = ShortFormatter('for (int i = 0; i < x.length; i++)')
    second_for.add_line('x[i] = Math.random() * 16.0 - 12.0')
    psvm.add_child(second_for)

    psvm.add_line('double[][] d = new double[14][20]')
    third_for_outer = ClassicFormatter('for (int i = 0; i < d.length; i++)')
    third_for_inner = ClassicFormatter('for (int j = 0; j < d[i].length; j++)')
    third_for_outer.add_child(third_for_inner)
    psvm.add_child(third_for_outer)

    switch = ClassicFormatter('switch ((int) b[i])')
    third_for_inner.add_child(switch)

    first_case = CaseFormatter('case 7')
    first_case.add_line('d[i][j] = Math.asin(Math.pow(Math.E, Math.cbrt(- Math.pow(Math.sin(x[j]), 2))))')
    switch.add_child(first_case)

    for number in [5, 6, 8, 9, 15, 16]:
        switch.add_line(f'case {number}', end=':')

    second_case = CaseFormatter('case 17')
    second_case.add_line('d[i][j] = Math.sin(Math.pow(3 * (Math.cos(x[j]) - 1), Math.pow(3 * x[j], 3)))')
    switch.add_child(second_case)

    default_case = CaseFormatter('default')
    default_case.add_line('d[i][j] = Math.pow(Math.E, Math.pow(Math.E, 4 * ((1 / 2) + x[j])))')
    switch.add_child(default_case)

    third_for_inner.add_line('System.out.printf("%.3f ", d[i][j])')

    third_for_outer.add_line('System.out.println()')

    result = public_class_main.get_result()

    for line in result:
        print(line, end='')
