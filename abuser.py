import os
import time
import yaml
import argparse


def run():

    def get_args() -> argparse.Namespace:

        parser = argparse.ArgumentParser()

        parser.add_argument('--config', type=str, help='a path to a config file', required=True)
        parser.add_argument('--rclone', type=str, help='a path to rclone binary on your computer', required=True)

        return parser.parse_args()

    def get_config() -> dict:

        with open(args.config, encoding='utf-8-sig') as yaml_file:
            result = yaml.safe_load(yaml_file)

        return result

    def print_elapsed_time(start_time):

        elapsed_time = time.time() - start_time
        elapsed_time = round(elapsed_time, 1)

        m, s = divmod(elapsed_time, 60)
        h, m = divmod(m, 60)

        h = round(h)
        m = round(m)
        s = round(s)

        print('--- {0}h {1}m {2}s ---'.format(h, m, s))

    start_time_for_script = time.time()

    args = get_args()
    config = get_config()
    command = '{} sync "{}" "{}" --copy-links --progress --stats-one-line'

    for config_line in config:

        sources = config_line.keys()

        for source in sources:

            target = config_line[source]

            print("Source: {}".format(source))
            print("Target: {}".format(target))

            start_time_for_source = time.time()

            os.system(command.format(args.rclone, source, target))

            print_elapsed_time(start_time_for_source)

            print()

    print_elapsed_time(start_time_for_script)


if __name__ == '__main__':
    run()
