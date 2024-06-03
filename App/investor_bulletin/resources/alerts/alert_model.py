""" Alert Model """
from sqlalchemy import Column, Integer, Float, DateTime, func
from db.models.model_base import Base

class Alert(Base):
    __tablename__ = "alerts"
    id = Column(Integer, primary_key=True, index=True)
    rule_id = Column(Integer)
    price = Column(Float)
    created_at = Column(DateTime, default=func.now())
