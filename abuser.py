"""
Consequently clones directories from a given list using rclone.
"""

import argparse
import logging
import os
import time

import yaml


def run() -> None:
    """
    Doing the mail script's objective (to clone listed directories).
    :return: nothing
    """

    def get_args() -> argparse.Namespace:
        parser = argparse.ArgumentParser()

        parser.add_argument(
            "--config", type=str, help="path to a config file", required=True
        )

        parser.add_argument(
            "--rclone",
            type=str,
            help='path to rclone binary ("rclone" by default)',
            default="rclone",
        )

        return parser.parse_args()

    def get_config() -> dict:
        with open(args.config, encoding="utf-8-sig") as yaml_file:
            result = yaml.safe_load(yaml_file)

        return result

    def get_logger() -> logging.Logger:
        def get_stream_handler():
            stream_handler = logging.StreamHandler()

            stream_handler.setLevel(logging.INFO)
            stream_handler.setFormatter(logging.Formatter("%(message)s"))

            return stream_handler

        result = logging.getLogger(__name__)

        result.setLevel(logging.INFO)
        result.addHandler(get_stream_handler())

        return result

    def print_elapsed_time(start_time: float):
        elapsed_time = time.time() - start_time
        elapsed_time = round(elapsed_time, 1)

        minutes, seconds = divmod(elapsed_time, 60)
        hours, minutes = divmod(minutes, 60)

        hours = round(hours)
        minutes = round(minutes)
        seconds = round(seconds)

        logger.info("Time taken: %sh %sm %ss\n", hours, minutes, seconds)

    start_time_for_script = time.time()

    args = get_args()
    config = get_config()
    logger = get_logger()
    command = '{} sync "{}" "{}" --copy-links --progress --stats-one-line'

    for source in config.keys():
        target = config[source]

        logger.info("Source: %s", source)
        logger.info("Target: %s", target)

        start_time_for_source = time.time()

        os.system(command.format(args.rclone, source, target))

        print_elapsed_time(start_time_for_source)

    print_elapsed_time(start_time_for_script)


if __name__ == "__main__":
    run()
