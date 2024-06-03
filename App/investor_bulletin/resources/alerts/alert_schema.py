""" Alert Schema """
"""_summary_
This file to abstract any validation logic for the Alerts
"""
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class AlertBase(BaseModel):
    rule_id: int
    price: float

class AlertCreate(AlertBase):
    pass

class Alert(AlertBase):
    id: int
    created_at: Optional[datetime]

    class Config:
        from_attributes = True
