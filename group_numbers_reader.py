class GroupNumbersReader:
    def __init__(self):
        self.numbers = []
        self.read_numbers()

    def read_numbers(self):
        with open('info/P3111_numbers.txt', 'r') as file:
            self.numbers = [line.replace('\n', '') for line in file.readlines()]
        print(self.numbers)

    def get_variant_by_last(self, count: int):
        result_list = []
        for old_elem in self.numbers:
            new_elem = int(old_elem[len(old_elem) - count:])
            result_list.append(new_elem)
        return result_list


def main():
    group_numbers_reader = GroupNumbersReader()
    variants = group_numbers_reader.get_variant_by_last(3)
    print(variants)


if __name__ == '__main__':
    main()
