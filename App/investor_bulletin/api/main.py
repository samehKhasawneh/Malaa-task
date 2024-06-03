from uu import Error
from uvicorn import run
from fastapi import FastAPI

from api.routes import init_routes

app = init_routes(FastAPI(
                        title="Task API",
                        docs_url='/api/docs',
                        redoc_url='/api/redoc',
                        openapi_url='/api/openapi.json'
                        )
                )

if __name__ == "__main__":
    run("api.main:app")
