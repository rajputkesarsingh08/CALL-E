from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.health import router as health_router
from app.routes.calls import router as calls_router

from app.database import Base, engine


app = FastAPI(
    title="CampusConnect AI",
    version="1.0.0",
    description="AI phone agent for student campus tasks."
)


app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:5500",
        "http://127.0.0.1:5500",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


Base.metadata.create_all(
    bind=engine
)


app.include_router(
    health_router,
    prefix="/api"
)


app.include_router(
    calls_router,
    prefix="/api"
)


@app.get("/")
def root():
    return {
        "name": "CampusConnect AI",
        "status": "running",
        "version": "1.0.0",
    }
