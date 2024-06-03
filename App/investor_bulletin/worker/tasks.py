from resources.alerts.alert_service import create_new_alerts
from resources.market.market_service import get_market_data
from worker.celery_app import celery_app
from core.messaging import publish_message
from resources.alert_rules.alert_rule_service import fetish_all_alert_rules
from db.models.model_base import get_db
from db.models import Alert


@celery_app.task
def fetch_market_data():
    rules_list = []
    with next(get_db()) as db:
        data = get_market_data()
        rules = fetish_all_alert_rules(db)
        if rules is None:
            return

        for rule in rules:
            current_price = data[rule.symbol]['values'][0]['close']
            if (float(current_price) > rule.threshold_price and 'high' in rule.name.lower()) or (float(current_price) < rule.threshold_price and 'low' in rule.name.lower()):
                publish_message('alerts_exchange', 'threshold.alert', f"Threshold alert for {rule.symbol} {rule.name}: {current_price}")
            rules_list.append(Alert(rule_id=rule.id, price=current_price))

        create_new_alerts(rules_list, db)
