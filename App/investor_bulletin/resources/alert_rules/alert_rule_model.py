""" Alert Rule Model """
from db.models.model_base import Base
from sqlalchemy import Column, Integer, String, Float, DateTime, func

class AlertRule(Base):
    __tablename__ = "alert_rules"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    threshold_price = Column(Float, index=True)
    symbol = Column(String, index=True)
    created_at = Column(DateTime, default=func.now())
