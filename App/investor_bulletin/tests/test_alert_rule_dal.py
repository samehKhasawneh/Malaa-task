import pytest
from sqlalchemy.orm import Session
from resources.alert_rules.alert_rule_schema import AlertRuleCreate
from resources.alert_rules.alert_rule_service import create_new_rule, fetish_all_alert_rules, get_alert_rule_by_id_service, update_alert_rule_service, delete_alert_rule_service

@pytest.fixture
def alert_rule_data():
    return AlertRuleCreate(name="Test Alert", threshold_price=100.0, symbol="AAPL")

def test_create_alert_rule(test_db: Session, alert_rule_data: AlertRuleCreate):
    alert_rule = create_new_rule(test_db, alert_rule_data)
    assert alert_rule.name == alert_rule_data.name
    assert alert_rule.threshold_price == alert_rule_data.threshold_price
    assert alert_rule.symbol == alert_rule_data.symbol

def test_get_alert_rule(test_db: Session, alert_rule_data: AlertRuleCreate):
    alert_rule = create_new_rule(test_db, alert_rule_data)
    fetched_alert_rule = get_alert_rule_by_id_service(test_db, alert_rule.id)
    assert fetched_alert_rule is not None
    assert fetched_alert_rule.name == alert_rule_data.name

def test_get_alert_rules(test_db: Session, alert_rule_data: AlertRuleCreate):
    create_new_rule(test_db, alert_rule_data)
    create_new_rule(test_db, alert_rule_data)
    fetched_alert_rule = fetish_all_alert_rules(test_db)
    assert len(fetched_alert_rule) > 0

def test_update_alert_rule(test_db: Session, alert_rule_data: AlertRuleCreate):
    alert_rule = create_new_rule(test_db, alert_rule_data)
    updated_data = AlertRuleCreate(name="Updated Alert", threshold_price=120.0, symbol="AAPL")
    updated_alert_rule = update_alert_rule_service(test_db, alert_rule.id, updated_data)
    assert updated_alert_rule.name == updated_data.name
    assert updated_alert_rule.threshold_price == updated_data.threshold_price
    assert updated_alert_rule.symbol == updated_data.symbol

def test_delete_alert_rule(test_db: Session, alert_rule_data: AlertRuleCreate):
    alert_rule = create_new_rule(test_db, alert_rule_data)
    delete_alert_rule_service(test_db, alert_rule.id)
    fetched_alert_rule = get_alert_rule_by_id_service(test_db, alert_rule.id)
    assert fetched_alert_rule is None
