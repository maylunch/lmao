from __future__ import annotations

from celery import Celery

from .core.config import settings

celery_app = Celery(
    "app",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
)

celery_app.conf.timezone = "UTC"
celery_app.conf.beat_schedule = {
    "fetch-market-data": {
        "task": "app.tasks.market.fetch_market_data",
        "schedule": settings.MARKET_FETCH_INTERVAL_MINUTES * 60,
    }
}

celery_app.autodiscover_tasks(["app.tasks"])