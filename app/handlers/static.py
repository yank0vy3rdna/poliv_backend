from starlette.staticfiles import StaticFiles

from app import app

app.mount("/", StaticFiles(directory="static", html=True), name="static")
