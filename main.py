from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import psutil

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def index():
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    return f"""
    <html><body>
    <h1>GpLehiy Zen</h1>
    <p>Нагрузка CPU: {cpu}%</p>
    <p>Память: {mem}%</p>
    <button>Подкинуть кожаного</button>
    <p>Сделай вдох и наблюдай за трафиком...</p>
    </body></html>
    """