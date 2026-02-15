# AI Global Chinese Portfolio

## Payment Callback

The VIP payment flow exposes an order creation endpoint and a callback endpoint under `/api/v1/vip`. Orders are stored in Redis with a `Pending` state and updated based on callback payloads. Callbacks must include a signature, timestamp, and nonce for verification. The callback handler performs:

- HMAC-SHA256 signature verification using `PAY_CALLBACK_SECRET`.
- Timestamp tolerance checks using `PAY_TIMESTAMP_TOLERANCE_SECONDS`.
- Nonce replay protection using `PAY_NONCE_TTL_SECONDS` in Redis.

Successful callbacks transition the order to `Paid`, while failures mark it as `Failed`.

## AI Analysis & Disclaimer

The `/api/v1/ai/analyze` endpoint builds a risk-analysis prompt and calls the configured AI model. The response is normalized to ensure required fields are present, and the disclaimer is enforced on every response. The disclaimer is mandatory and indicates that the analysis is for reference only and does not constitute investment advice.

Relevant settings:

- `AI_API_URL`
- `AI_API_KEY`
- `AI_MODEL`

## Market Data Fetching & Celery

Market data is fetched on a schedule via Celery and stored in Redis for quick access. The Celery app is configured in `backend/app/celery_app.py` and schedules the `app.tasks.market.fetch_market_data` task at the interval defined by `MARKET_FETCH_INTERVAL_MINUTES`.

Key settings:

- `MARKET_DATA_URL`
- `MARKET_FETCH_SYMBOLS`
- `MARKET_FETCH_INTERVAL_MINUTES`
- `CELERY_BROKER_URL`
- `CELERY_RESULT_BACKEND`

To run the scheduler, start a Celery worker and beat process pointing to the `app.celery_app` module.
