import yaml

#IMPORTANT because we are reading from the disk we do not want to read from the
#disk every time we are opening the file config.yaml so this helps us to
#prevent this
__config = None

def config():
    global __config
    if not __config:
        with open('config.yaml', mode = 'r') as f:
            __config = yaml.safe_load(f)

    return __config
