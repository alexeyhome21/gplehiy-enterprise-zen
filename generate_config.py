import json
from pathlib import Path

TEMPLATE_PATH = Path('config_template.json')
USERS_PATH = Path('users.json')
CONFIG_PATH = Path('config.json')


def generate():
    template = json.loads(TEMPLATE_PATH.read_text())
    users = json.loads(USERS_PATH.read_text())
    template['inbounds'][0]['settings']['clients'] = [
        {'id': u['uuid'], 'email': u['name']} for u in users
    ]
    CONFIG_PATH.write_text(json.dumps(template, indent=2))


if __name__ == '__main__':
    generate()
