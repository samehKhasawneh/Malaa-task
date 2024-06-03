""" Alert Rule  DAL"""
"""_summary_
this file is to right any ORM logic for the Alert Rule model
"""
from resources.alert_rules.alert_rule_schema import AlertRuleCreate
from db.models import AlertRule
from sqlalchemy.orm import Session

def create_alert_rule( rule: AlertRuleCreate, session: Session):
    new_rule = AlertRule(**rule.dict())
    session.add(new_rule)
    session.commit()
    session.refresh(new_rule)
    return new_rule

def fetish_alert_rules(session: Session):
    return session.query(AlertRule).all()

def delete_alert_rule(session: Session, id: int):
    session.query(AlertRule).filter(AlertRule.id == id).delete()
    session.commit()
    return

def update_alert_rule(session: Session, id: int, rule:AlertRuleCreate):
    alert = session.query(AlertRule).filter(AlertRule.id == id).first()
    if alert is None:
        return {"error": "Alert rule not found"}
    alert.name = rule.name
    alert.threshold_price = rule.threshold_price
    alert.symbol = rule.symbol
    session.commit()
    session.refresh(alert)
    return alert

def get_alert_rule_by_id(session: Session, id: int):
    return session.query(AlertRule).filter(AlertRule.id == id).first()
