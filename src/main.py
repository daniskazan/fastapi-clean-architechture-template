import fastapi
import uvicorn

from api.routing import router
from config import app_config

app = fastapi.FastAPI()

app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=app_config.APP_HOST,
        port=app_config.APP_PORT,
        workers=app_config.UVICORN_WORKERS,
    )
