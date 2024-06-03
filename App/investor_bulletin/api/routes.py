from api.controllers.market_controllers import router as MarketRouter
from api.controllers.rules_controller import router as RuleRouter

def init_routes(app):
    app.include_router(MarketRouter, prefix="/market", tags=["Market"])
    app.include_router(RuleRouter, prefix="/alert", tags=["Alert"])
    return app
