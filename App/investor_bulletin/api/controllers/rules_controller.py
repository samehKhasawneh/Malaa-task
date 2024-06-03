from typing import List
from resources.alerts.alert_service import fetish_all_alerts
from resources.alert_rules.alert_rule_schema import  AlertRuleCreate, AlertRule as AlertRuleSchema
from resources.alerts.alert_schema import Alert as AlertSchema
from resources.alert_rules.alert_rule_service import create_new_rule, fetish_all_alert_rules, delete_alert_rule_service, update_alert_rule_service

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.models.model_base import get_db

router = APIRouter()



@router.post("/alert-rules", response_model=AlertRuleSchema)
def create_alert_rule(alert: AlertRuleCreate, db: Session = Depends(get_db)):
    alert = AlertRuleCreate(name=alert.name, threshold_price=alert.
    threshold_price, symbol=alert.symbol)
    return create_new_rule(db, alert)

@router.get("/alert-rules", response_model=List[AlertRuleSchema])
def get_alert_rules(db: Session = Depends(get_db)):
    return fetish_all_alert_rules(db)

@router.patch("/alert-rules/{id}", response_model=AlertRuleSchema)
def update_alert_rule(id: int, alert: AlertRuleCreate, db: Session = Depends(get_db)):
    alert = AlertRuleCreate(name=alert.name, threshold_price=alert.
    threshold_price, symbol=alert.symbol)
    return update_alert_rule_service(db, id, alert)


@router.delete("/alert-rules/{id}")
def delete_alert_rule(id: int, db: Session = Depends(get_db)):
    delete_alert_rule_service(db, id)
    return {"message": "Alert rule deleted"}


@router.get("/alerts", response_model=List[AlertSchema])
def get_alerts(db: Session = Depends(get_db)):
    return fetish_all_alerts(db)
