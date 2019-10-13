from collections import deque


class FormulaConverter:
    @staticmethod
    def __find_bracets(s: str, start_position: int, revers: bool = False):
        everything = ''
        brackets = deque()

        used_range = range(start_position, len(s))
        if revers:
            used_range = range(start_position, -1, -1)

        appending_elem, popping_elem = '(', ')'
        if revers:
            appending_elem, popping_elem = ')', '('

        first_symbol_flag = True
        checking_flag = ''

        for i in used_range:
            char = s[i]

            everything += char

            if first_symbol_flag:
                if char == appending_elem:
                    checking_flag = 'brackets'
                else:
                    checking_flag = 'ending'
                first_symbol_flag = False

            if checking_flag == 'brackets':
                if char == appending_elem:
                    brackets.append(appending_elem)
                elif char == popping_elem:
                    brackets.popleft()
                    if len(brackets) == 0:
                        if revers:
                            not_arc = s[i - 1:i - 4:-1][::-1]
                            if not_arc in ['sin', 'cos']:
                                everything += not_arc[::-1]

                            arc = s[i - 1:i - 7:-1][::-1]
                            if arc in ['arcsin', 'arccos']:
                                everything += arc[::-1]

                        break
            elif checking_flag == 'ending':
                if char == appending_elem or char == popping_elem:
                    everything = everything[:-1]
                    break

        if revers:
            everything = everything[::-1]
        return everything

    @staticmethod
    def __find_right(s: str, start_position: int):
        return FormulaConverter.__find_bracets(s, start_position, False)

    @staticmethod
    def __find_left(s: str, start_position: int):
        return FormulaConverter.__find_bracets(s, start_position, True)

    @staticmethod
    def __replace_to_pow_trigonometry(s: str):
        # matches = []
        # for trigonometry_function in ['sin', 'cos', 'arcsin', 'arccos']:
        #     matches += [m.start() for m in re.finditer(f'{trigonometry_function}\^', s)]

        for trigonometry_function in ['sin', 'cos', 'arcsin', 'arccos']:
            match_index = -1
            while True:
                match_index = s.find(f'{trigonometry_function}^', match_index + 1)
                if match_index == -1:
                    break
                start = s.find('^', match_index)
                first = FormulaConverter.__find_right(s, start + 1)
                second = FormulaConverter.__find_right(s, start + 1 + len(first))

                old = f'^{first}{second}'
                new = f'{second}^{first}'
                s = s.replace(old, new)

        return s

    @staticmethod
    def __replace_to_pow_usual(s: str):
        # matches = [m.start() for m in re.finditer('\^', s)]
        match_index = -1
        while True:
            match_index = s.find('^', match_index + 1)
            if match_index == -1:
                break
            start = s.find('^', match_index)
            left = FormulaConverter.__find_left(s, start - 1)
            right = FormulaConverter.__find_right(s, start + 1)
            old = f'{left}^{right}'
            new = f'Math.pow({left}, {right})'
            s = s.replace(old, new)
        return s

    @staticmethod
    def replace_to_pow(s: str):
        s = FormulaConverter.__replace_to_pow_trigonometry(s)
        s = FormulaConverter.__replace_to_pow_usual(s)
        return s

    @staticmethod
    def replace_other(s: str):
        s = s.replace('x', 'x[j]')

        s = s.replace('e', 'Math.E')
        s = s.replace('pi', 'Math.PI')

        s = s.replace('abs', 'Math.abs')
        s = s.replace('ln', 'Math.log')

        s = s.replace('root(2)', 'Math.sqrt')
        s = s.replace('root(3)', 'Math.cbrt')

        s = s.replace('arcsin', 'Math.asiN')
        s = s.replace('arccos', 'Math.acoS')
        s = s.replace('arctan', 'Math.ataN')

        s = s.replace('sin', 'Math.sin')
        s = s.replace('cos', 'Math.cos')
        s = s.replace('tan', 'Math.tan')

        s = s.replace('Math.asiN', 'Math.asin')
        s = s.replace('Math.acoS', 'Math.acos')
        s = s.replace('Math.ataN', 'Math.atan')

        return s

    @staticmethod
    def convert_formula(s: str):
        s = FormulaConverter.replace_to_pow(s)
        s = FormulaConverter.replace_other(s)
        return s


def main():
    s = 'e^(e^(4*(1/2+x)))+1/2'

    # s = 'arcsin(e^(root(3)(-sin^2(x))))'
    # s = 'ln(sin^2((1/3/(3/4+x)/x)^2))'

    # s = 'sin((3*(cos(x)-1))^((3*x)^3))'
    # s = 'e^(e^(4*(1/2+x)))+1/2'

    print(s)
    result = FormulaConverter.convert_formula(s)
    print(result)


if __name__ == '__main__':
    main()
