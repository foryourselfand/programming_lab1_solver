from task_inputs import TaskInputsCreator
from variant_getter import VariantGetter
from writer import TaskWriter
from sys import argv


def main():
    variant = int(argv[1]) if len(argv) == 2 else 24092000

    variant_getter = VariantGetter()

    task_inputs_creator = TaskInputsCreator(variant_getter)
    input_tasks = task_inputs_creator.get_task_inputs(variant)

    task_writer = TaskWriter()
    task_writer.write_task(input_tasks, variant)

    variant_getter.dump_remembered_variants()


if __name__ == '__main__':
    main()
