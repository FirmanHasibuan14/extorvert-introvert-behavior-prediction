from sqlalchemy import Column, Integer, String, Float
from database.database import Base

class PredictionLog(Base):
    __tablename__ = "prediction_logs"

    id = Column(Integer, primary_key=True, index=True)
    time_spent_alone = Column(Float)
    
    stage_fear = Column(Integer) 
    
    social_event_attendance = Column(Float)
    going_outside = Column(Float)
    
    drained_after_socializing = Column(Integer) 
    
    friends_circle_size = Column(Float)
    post_frequency = Column(Float)
    predicted_personality = Column(String)