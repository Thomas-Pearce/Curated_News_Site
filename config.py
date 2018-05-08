import yaml

__CONFIG__ = None

def get_config():
    global __CONFIG__
    if __CONFIG__ is None:
        with open('config.yml', encoding='utf-8') as f:
            contents = f.read()

            __CONFIG__ = yaml.load(contents)
    return __CONFIG__

