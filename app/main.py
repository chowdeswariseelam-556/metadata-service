
from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base
from app.api.routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Metadata Service")

app.include_router(router)
