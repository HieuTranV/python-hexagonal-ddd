from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.infrastructure.middleware.trace_id import TraceIDMiddleware
from .config import config
from .routers import user, product
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(TraceIDMiddleware)

app.include_router(user.router)
app.include_router(product.router)
# Instantiate repositories and services