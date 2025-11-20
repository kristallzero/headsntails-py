import json


def load():
    try:
        with open('data.json') as f:
            config = json.load(f)
            if type(config) == dict:
                return config
            else:
                return {}
    except:
        return {}


def save(config):
    try:
        with open('data.json', 'w') as f:
            json.dump(config if type(config) == dict else {}, f)
    except:
        with open('data.json', 'w') as f:
            f.write('{}')
