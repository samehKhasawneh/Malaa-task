""" Rule Service"""
"""_summary_
this file to write any business logic for the Rules
"""
from typing import List
from db.models import Alert
from resources.alerts.alert_schema import AlertCreate
from resources.alerts.alert_dal import create_alert, create_alerts, fetish_alerts
from sqlalchemy.orm import Session

def create_new_alert( alert: AlertCreate,  db: Session ):
    return create_alert( alert=alert, db=db)

def create_new_alerts(alerts: List[Alert], db: Session):
    return create_alerts(alerts=alerts, db=db)

def fetish_all_alerts(db: Session):
    return fetish_alerts(db=db)
