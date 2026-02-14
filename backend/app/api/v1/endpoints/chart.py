from fastapi import APIRouter

router = APIRouter()

@router.get("/industry")
def industry():
    return {"data": []}

@router.get("/market")
def market():
    return {"data": []}

@router.get("/performance")
def performance(period: str = "1y"):
    return {"period": period, "data": []}