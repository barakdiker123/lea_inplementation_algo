from local_search_algorithm import create_instance
import local_search_algorithm
import argparse
import os
import logging

formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")


def setup_logger(name, log_file, level=logging.DEBUG):
    """To setup as many loggers as you want"""

    # open(log_file, "a").close()
    # open(log_file, "w").close()
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


def dir_path(string):
    if os.path.exists(string):
        return string
    else:
        raise NotADirectoryError(string)


def init():
    parser = argparse.ArgumentParser("simple_example")
    parser.add_argument(
        "--animation_flag",
        action="store_true",
        help="For animation add the --animation_flag flag ! ",
    )
    parser.add_argument(
        "--visualize_simple",
        action="store_true",
        help="For visualizing add the --visualize_simple flag ! ",
    )
    parser.add_argument(
        "--input_path",
        type=dir_path,
        help='path to input file for example "test/input/input.py" \n the input.py should have the format \n \
        m = 6 \n \
        k=5 \n processing_arr = [2, 3, 3, 4, 4, 4, 5, 5, 5, 5]',
        default="test/input/input.py",
    )
    parser.add_argument(
        "--output_dir",
        help="A path to put all the output files ",
        default="test",
        # type=dir_path,
    )
    args = parser.parse_args()
    name = args.output_dir
    logger1 = setup_logger(
        "myapp.area1", name + "/output/" + "finding_minimum_with_local_search.log"
    )
    # logger1 = logging.getLogger("myapp.area1")
    logger2 = setup_logger(
        "myapp.area2",
        name + "/output/" + "after_finding_the_smallest_do_the_replacement.log",
    )
    # logger2 = logging.getLogger("myapp.area2")
    # print(args.input_path)

    # if args.visualize_simple:
    #    print("Barak")

    create_instance(
        args.output_dir,
        args.input_path,
        args.visualize_simple,
        args.animation_flag,
        logger1,
        logger2,
    )


if __name__ == "__main__":
    init()
