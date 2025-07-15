from fastapi import FastAPI, Request, Form, Depends, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import uuid
import json
import psutil
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

app = FastAPI()
security = HTTPBasic()

USERS_PATH = Path('users.json')

env = Environment(loader=FileSystemLoader('.'))

def load_users():
    if USERS_PATH.exists():
        return json.loads(USERS_PATH.read_text())
    return []

def save_users(users):
    USERS_PATH.write_text(json.dumps(users, indent=2))


def get_stats():
    return psutil.cpu_percent(), psutil.virtual_memory().percent


def check_auth(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username == 'admin' and credentials.password == 'admin':
        return True
    raise HTTPException(status_code=401)


@app.get('/', response_class=HTMLResponse)
async def index(credentials: HTTPBasicCredentials = Depends(check_auth)):
    users = load_users()
    cpu, mem = get_stats()
    tmpl = env.get_template('templates/index.html')
    return tmpl.render(users=users, cpu=cpu, mem=mem)


@app.post('/add_user')
async def add_user(name: str = Form(...), credentials: HTTPBasicCredentials = Depends(check_auth)):
    users = load_users()
    new_user = {'name': name, 'uuid': str(uuid.uuid4())}
    users.append(new_user)
    save_users(users)
    import generate_config
    generate_config.generate()
    return RedirectResponse('/', status_code=302)
