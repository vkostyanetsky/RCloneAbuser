import argparse
import logging
import os
import time

import yaml


def run():
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

        m, s = divmod(elapsed_time, 60)
        h, m = divmod(m, 60)

        h = round(h)
        m = round(m)
        s = round(s)

        logger.info("Time taken: {0}h {1}m {2}s\n".format(h, m, s))

    start_time_for_script = time.time()

    args = get_args()
    config = get_config()
    logger = get_logger()
    command = '{} sync "{}" "{}" --copy-links --progress --stats-one-line'

    for source in config.keys():

        target = config[source]

        logger.info("Source: {}".format(source))
        logger.info("Target: {}".format(target))

        start_time_for_source = time.time()

        os.system(command.format(args.rclone, source, target))

        print_elapsed_time(start_time_for_source)

    print_elapsed_time(start_time_for_script)


if __name__ == "__main__":
    run()
