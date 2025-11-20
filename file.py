import json


def load() -> dict:
    try:
        with open('data.json') as f:
            config = json.load(f)
            if isinstance(config, dict):
                return config
            else:
                return {}
    except:
        return {}


def save(config: dict) -> None:
    try:
        with open('data.json', 'w') as f:
            json.dump(config if isinstance(config, dict) else {}, f)
    except:
        with open('data.json', 'w') as f:
            f.write('{}')
