"""
main.py
-------
FastAPI main application with all endpoints.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from src.api.routes import forecasts, anomalies, optimization, health
from src.database.db_config import engine, Base
from src.utils.logger import get_logger
from src.utils.config import config

logger = get_logger(__name__)

# Create tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(
    title="Airport Operations AI API",
    description="Advanced forecasting, anomaly detection, and optimization API",
    version="2.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health.router, prefix="/api", tags=["Health"])
app.include_router(forecasts.router, prefix="/api", tags=["Forecasts"])
app.include_router(anomalies.router, prefix="/api", tags=["Anomalies"])
app.include_router(optimization.router, prefix="/api", tags=["Optimization"])


@app.on_event("startup")
async def startup_event():
    """Initialize on startup."""
    logger.info("Airport Operations API starting up...")
    config.ensure_dirs()


@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown."""
    logger.info("Airport Operations API shutting down...")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
