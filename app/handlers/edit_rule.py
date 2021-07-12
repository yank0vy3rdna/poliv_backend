from fastapi import Depends, HTTPException, status

from app import app

from pydantic import BaseModel

from app.models import User, Rule
from app.services.auth import get_current_user


class RuleModel(BaseModel):
    hour: int
    minute: int


@app.patch('/rule/{device_id}')
async def h(device_id: int, rule_id: int, note: RuleModel, current_user: User = Depends(get_current_user)):
    rule_db = await Rule.filter(id=rule_id, device_id=device_id).first()
    if not rule_db:
        rule_db = await Rule.create(device_id=device_id, hour=note.hour, minute=note.minute)
    else:
        rule_db.hour = note.hour
        rule_db.minute = note.minute
        await rule_db.save()
    return rule_db.to_dict()
