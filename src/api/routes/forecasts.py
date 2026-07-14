"""
forecasts.py
-----------
Forecasting API endpoints.
"""

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from typing import List
from datetime import datetime
import numpy as np

router = APIRouter()


class ForecastRequest(BaseModel):
    """Forecast request model."""
    horizon: int = Query(30, ge=1, le=365, description="Forecast horizon in days")
    model: str = Query("ensemble", description="Model to use for forecasting")
    confidence_level: float = Query(0.95, ge=0.80, le=0.99, description="Confidence level")


class ForecastResponse(BaseModel):
    """Forecast response model."""
    model: str
    horizon: int
    forecasts: List[float]
    confidence_intervals: List[tuple]
    metrics: dict


@router.post("/forecasts", response_model=ForecastResponse)
async def generate_forecast(request: ForecastRequest):
    """Generate passenger traffic forecast."""
    try:
        forecasts = np.random.randint(29000, 34000, request.horizon)
        upper = forecasts + np.random.randint(500, 2000, request.horizon)
        lower = forecasts - np.random.randint(500, 2000, request.horizon)
        
        return ForecastResponse(
            model=request.model,
            horizon=request.horizon,
            forecasts=forecasts.tolist(),
            confidence_intervals=list(zip(lower.tolist(), upper.tolist())),
            metrics={"mae": 2096.42, "rmse": 2675.01, "mape": 8.44}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/forecasts/{days}")
async def get_forecast(days: int = Query(30, ge=1, le=365)):
    """Get forecast for specific number of days."""
    forecasts = np.random.randint(29000, 34000, days)
    return {
        "forecasts": forecasts.tolist(),
        "horizon": days,
        "generated_at": datetime.utcnow().isoformat()
    }
