""" Alert Rule Schema """
"""_summary_
This file to abstract any validation logic for the Alert Rules
"""
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AlertRuleBase(BaseModel):
    name: str
    threshold_price: float
    symbol: str

class AlertRuleCreate(AlertRuleBase):
    pass

class AlertRule(AlertRuleBase):
    id: int
    created_at: Optional[datetime]

    class Config:
        from_attributes = True
