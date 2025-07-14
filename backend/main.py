from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
from routers import story, job
from db.database import create_tables

create_tables()

app = FastAPI(
    title="Choose Your Own Adventure Game API",
    description="api to generate cool stories",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add our middleware - have our api used from different origins.
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,  # from localhost or from other frontend online.
    allow_credentials=True,
    allow_methods=["*"],  # GET, POST, PUT, DELETE
    allow_headers=["*"],  # Additional information to send with request
)

app.include_router(story.router, prefix=settings.API_PREFIX)
app.include_router(job.router, prefix=settings.API_PREFIX)

if __name__ == "__main__":
    # standard python practice - it means only execute what's inside this if statement.
    # If we directly execute this python file.

    # uvicorn is a web server - allows us to serve our FastAPI application
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
