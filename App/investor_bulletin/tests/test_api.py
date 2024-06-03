import pytest

def test_create_alert_rule(client):
    alert_rule_data = {
        "name": "Test Alert",
        "threshold_price": 100.0,
        "symbol": "AAPL"
    }
    response = client.post("/alert/alert-rules", json=alert_rule_data)
    assert response.status_code == 200
    assert response.json()["name"] == alert_rule_data["name"]

def test_get_alert_rules(client):
    response = client.get("/alert/alert-rules")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_alert_rule(client):
    alert_rule_data = {
        "name": "Updated Alert",
        "threshold_price": 120.0,
        "symbol": "AAPL"
    }

    rules_response = client.get("/alert/alert-rules")
    id = rules_response.json()[0]['id']
    response = client.patch(f"/alert/alert-rules/{id}", json=alert_rule_data)

    assert response.status_code == 200
    assert response.json()["name"] == alert_rule_data["name"]

def test_delete_alert_rule(client):
    # Assume an alert rule with id 1 exists
    response = client.delete("/alert/alert-rules/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Alert rule deleted"

def test_get_alerts(client):
    response = client.get("/alert/alerts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
