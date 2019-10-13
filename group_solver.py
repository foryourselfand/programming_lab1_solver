from task_inputs import TaskInputsCreator
from variant_getter import VariantGetter
from writer import TaskWriter
from group_numbers_reader import GroupNumbersReader


def main():
    variant_getter = VariantGetter()

    task_inputs_creator = TaskInputsCreator(variant_getter)

    group_numbers_reader = GroupNumbersReader()
    variants = group_numbers_reader.get_variant_by_last(3)
    task_writer = TaskWriter()

    for new_variant in variants:
        input_tasks = task_inputs_creator.get_task_inputs(new_variant)
        task_writer.write_task(input_tasks, new_variant)

    variant_getter.dump_remembered_variants()


if __name__ == '__main__':
    main()
