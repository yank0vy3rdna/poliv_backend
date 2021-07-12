from fastapi import Depends

from app import app
from app.models import Device, User
from app.services.auth import get_current_user


@app.post('/switch/{device_id}')
async def h(device_id: int, user: User = Depends(get_current_user)):
    device = await Device.get(id=device_id)
    device.enabled = not device.enabled
    await device.save()
    return device.to_dict()
