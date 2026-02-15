from __future__ import annotations

from celery.utils.log import get_task_logger

from ..celery_app import celery_app
from ..services.market_data import MarketDataService

logger = get_task_logger(__name__)

@celery_app.task(name="app.tasks.market.fetch_market_data")
def fetch_market_data() -> dict:
    service = MarketDataService()
    records = service.fetch()
    if records:
        service.cache_latest(records)
    logger.info("Fetched %s market records", len(records))
    return {"count": len(records)}