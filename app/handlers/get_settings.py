import datetime

from fastapi import HTTPException, status
from fastapi.responses import Response

from app import app
from app.models import Device, Rule
from app.services import config


@app.get('/get_settings/{unique_str}/{info_from_device}')
async def h(unique_str: str, info_from_device: str):
    device = await Device.get(unique_str=unique_str)
    if not device:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Device with that unique_str not found",
        )
    device.info_from_device = info_from_device + 'date=' + str(datetime.datetime.now())
    await device.save()
    rules = await Rule.filter(device=device)
    rules = [rule.hour * 60 + rule.minute for rule in rules]
    rules.sort()
    settings_str = [1 if device.enabled else 0, len(rules) * 4]
    for rule in rules:
        if rule + config.TIME_OF_NABOR + config.TIME_OF_POLIV <= 24 * 60:
            settings_str.append(rule - (rule >> 8 << 8))  # little-endian uint16_t
            settings_str.append(rule >> 8)
            settings_str.append(config.POLIV_RELAY_PIN)
            settings_str.append(1)

            rule += config.TIME_OF_POLIV
            settings_str.append(rule - (rule >> 8 << 8))  # little-endian uint16_t
            settings_str.append(rule >> 8)
            settings_str.append(config.POLIV_RELAY_PIN)
            settings_str.append(0)

            settings_str.append(rule - (rule >> 8 << 8))  # little-endian uint16_t
            settings_str.append(rule >> 8)
            settings_str.append(config.NABOR_RELAY_PIN)
            settings_str.append(1)

            rule += config.TIME_OF_NABOR
            settings_str.append(rule - (rule >> 8 << 8))  # little-endian uint16_t
            settings_str.append(rule >> 8)
            settings_str.append(config.NABOR_RELAY_PIN)
            settings_str.append(0)
    settings_str.extend([0] * (162 - len(settings_str)))
    return Response(content=bytes(settings_str), media_type="application/macbinary")
