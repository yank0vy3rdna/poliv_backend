from fastapi import Depends

from app import app
from app.models import Device, User
from app.services.auth import get_current_user


@app.get('/rules/{device_id}')
async def h(device_id: int, user: User = Depends(get_current_user)):
    device = await Device.get(id=device_id).prefetch_related("rules")
    return [i.to_dict() for i in device.rules]
