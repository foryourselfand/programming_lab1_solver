from abc import abstractmethod
from typing import List, Union


class TabFormatter(object):
    def __init__(self, header):
        self.elems: List[Union[str, TabFormatter]] = list()

        self.final_result = []
        self.final_result.append(f'{header}{self.get_header_start()}\n')

    def add(self, elem, end: str = ';'):
        if type(elem) == str:
            self.elems.append(f'\t{elem}{end}\n')
        else:
            self.elems.append(elem)

    def get_result(self):
        for elem in self.elems:
            if type(elem) == str:
                self.final_result.append(elem)
            else:
                child_results = elem.get_result()
                for child_result in child_results:
                    self.final_result.append(f'\t{child_result}')
        self.final_result.append(self.get_header_end())
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
        return '}\n'


class ShortFormatter(TabFormatter):
    def get_header_start(self) -> str:
        return ''

    def get_header_end(self) -> str:
        return ''


class CaseFormatter(TabFormatter):
    def get_header_start(self) -> str:
        return ':'

    def get_header_end(self) -> str:
        return '\tbreak;\n'


def main():
    public_class_main = ClassicFormatter('public class Main')

    psvm = ClassicFormatter('public static void main(String[] args)')
    psvm.add('short[] b = {18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5}')
    public_class_main.add(psvm)

    psvm.add('double[] x = new double[20]')
    second_for = ShortFormatter('for (int i = 0; i < x.length; i++)')
    second_for.add('x[i] = Math.random() * 16.0 - 12.0')
    psvm.add(second_for)

    psvm.add('double[][] d = new double[14][20]')
    third_for_outer = ClassicFormatter('for (int i = 0; i < d.length; i++)')
    third_for_inner = ClassicFormatter('for (int j = 0; j < d[i].length; j++)')
    third_for_outer.add(third_for_inner)
    psvm.add(third_for_outer)

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

    result = public_class_main.get_result()

    for line in result:
        print(line, end='')


if __name__ == '__main__':
    main()
