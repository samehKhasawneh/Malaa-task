from fastapi import APIRouter
from resources.market.market_service import get_market_data
router = APIRouter()

@router.get("/market-prices")
async def get_market_data_route():
    return get_market_data()
