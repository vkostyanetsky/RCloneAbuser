import os
import sys
import time
import yaml

def print_time(s):

    m, s = divmod(s, 60)
    h, m = divmod(m, 60)

    h = round(h)
    m = round(m)
    s = round(s)

    print('--- {0}:{1}:{2} ---'.format(h, m, s))

def get_config():

    def get_config_path():

        script_dir  = os.path.abspath(os.path.dirname(__file__))
        
        return os.path.join(script_dir, 'config.yaml')

    def get_data_from_yaml(yaml_filepath):

        with open(yaml_filepath, encoding = 'utf-8-sig') as yaml_file:
            result = yaml.safe_load(yaml_file)

        return result

    config_path = get_config_path()

    return get_data_from_yaml(config_path)

def get_plans():

    def get_script_parameter_value(name, default_value):
                
        result = default_value
        
        for i, value in enumerate(sys.argv):

            if value == name and len(sys.argv) > i:

                result = sys.argv[i + 1]
                break

        return result

    plans = get_script_parameter_value('--plans', None)

    if plans != None:
        plans = plans.split(',')

    return plans

def rclone():

    command = 'rclone sync "{0}" "{1}" --copy-links --progress --stats-one-line'.format(source, target)     
    
    os.system(command)

config  = get_config()
plans   = get_plans()

if plans == None:
    exit()

elapsed_time_total = 0

for plan in plans:

    for paths in config[plan]:
        
        sources = paths.keys()

        for source in sources:

            target = paths[source]            

            print('Source: %s' % source)  
            print('Target: %s' % target)

            start_time = time.time()

            rclone()

            elapsed_time = time.time() - start_time
            elapsed_time = round(elapsed_time, 1)

            print_time(elapsed_time)
            print('')

            elapsed_time_total += elapsed_time

print_time(elapsed_time_total)