from fastapi import Depends

from app import app
from app.models import Device, User
from app.services.auth import get_current_user


@app.get('/devices')
async def h(user: User = Depends(get_current_user)):
    devices = await Device.filter()
    return [i.to_dict() for i in devices]
