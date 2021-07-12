from fastapi.logger import logger
from tortoise import Tortoise, exceptions
from tortoise.backends.base.config_generator import generate_config

from app import app
from app.services import config

tortoise_config: dict = generate_config(config.POSTGRES_URI, {"models": ["app.models"]})


def describe_credentials():
    described_models: dict = tortoise_config
    for database in described_models.get("connections"):
        source_pass = config.POSTGRES_PASSWORD
        if len(source_pass) > 0:
            hided_pass = source_pass[0] + "*" * len(source_pass[1:-1]) + source_pass[-1]
            described_models["connections"][database]["credentials"]["password"] = hided_pass

    return described_models


@app.on_event("startup")
async def on_startup():
    try:
        await Tortoise.init(
            config=tortoise_config,
        )
        await Tortoise.generate_schemas()
        logger.info("PostgreSQL Connection opened")
        logger.info(describe_credentials())
    except exceptions.ConfigurationError as e:
        logger.error(f"Database initialization error: {e}")
    except ConnectionError as e:
        logger.error(f"Database initialization error: {e}")


@app.on_event("shutdown")
async def on_shutdown():
    await Tortoise.close_connections()  # it will raise logging info
