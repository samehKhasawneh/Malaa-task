from db.models.model_base import SessionLocal
from resources.alert_rules.alert_rule_model import AlertRule


def seed_data():
    db = SessionLocal()
    initial_alerts = [
        {"name": "AAPL High", "threshold_price": 192.0, "symbol": "AAPL"},
        {"name": "AAPL Low", "threshold_price": 180.0, "symbol": "AAPL"},
        {"name": "MSFT High", "threshold_price": 413.0, "symbol": "MSFT"},
        {"name": "MSFT Low", "threshold_price": 400.0, "symbol": "MSFT"},
        {"name": "GOOG High", "threshold_price": 173.0, "symbol": "MSFT"},
        {"name": "GOOG Low", "threshold_price": 163.0, "symbol": "MSFT"},
        {"name": "AMZN High", "threshold_price": 175.0, "symbol": "MSFT"},
        {"name": "AMZN Low", "threshold_price": 165.0, "symbol": "MSFT"},
        {"name": "META High", "threshold_price": 465.0, "symbol": "MSFT"},
        {"name": "META Low", "threshold_price": 435.0, "symbol": "MSFT"}
    ]
    for alert in initial_alerts:
        db_alert = AlertRule(**alert)
        db.add(db_alert)
    db.commit()
    db.close()

seed_data()
