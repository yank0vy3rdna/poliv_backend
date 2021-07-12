from fastapi import Depends

from app import app
from app.models import Device, User, Rule
from app.services.auth import get_current_user


@app.get('/rule/{device_id}/{rule_id}')
async def h(device_id: int, rule_id: int, user: User = Depends(get_current_user)):
    return (await Rule.filter(id=rule_id, device_id=device_id).first()).to_dict()
