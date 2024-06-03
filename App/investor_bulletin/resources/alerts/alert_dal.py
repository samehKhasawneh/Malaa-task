""" Alert DAL"""
"""_summary_
this file is to right any ORM logic for the Alert model
"""
from typing import List
from resources.alerts.alert_schema import AlertCreate
from db.models import Alert
from sqlalchemy.orm import Session

def create_alert( alert: AlertCreate,  db: Session ):
    new_alert = Alert(**alert.dict())
    db.add(new_alert)

def create_alerts(alerts: List[Alert], db: Session):
    db.bulk_save_objects(alerts)
    db.commit()

def fetish_alerts( db: Session):
    return db.query(Alert).all()
