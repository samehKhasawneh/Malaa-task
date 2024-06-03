""" Alert Rule Service"""
"""_summary_
this file to write any business logic for the Alert Rules
"""
from resources.alert_rules.alert_rule_schema import AlertRuleCreate, AlertRule
from resources.alert_rules.alert_rule_dal import create_alert_rule, fetish_alert_rules, delete_alert_rule, get_alert_rule_by_id, update_alert_rule
from sqlalchemy.orm import Session


def create_new_rule(db: Session, rule: AlertRuleCreate):
    return create_alert_rule( rule=rule, session=db)

def fetish_all_alert_rules(db: Session):
    return fetish_alert_rules(session=db)


def delete_alert_rule_service(db: Session, id: int):
    delete_alert_rule(db, id)
    return

def update_alert_rule_service(db: Session, id: int, rule: AlertRuleCreate):
    return update_alert_rule(db, id, rule)

def get_alert_rule_by_id_service(db: Session, id: int):
    return get_alert_rule_by_id(db, id)
