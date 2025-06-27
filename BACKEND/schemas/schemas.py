from pydantic import BaseModel
from typing import List
from enum import Enum

class YesNoEnum(str, Enum):
    yes = 'Yes'
    no = 'No'

class PersonalityEnum(str, Enum):
    introvert = 'Introvert'
    extrovert = 'Extrovert'

class PersonalityFeatures(BaseModel):
    Time_spent_Alone: float
    Stage_fear: YesNoEnum
    Social_event_attendance: float
    Going_outside: float
    Drained_after_socializing: YesNoEnum 
    Friends_circle_size: float
    Post_frequency: float

class PredictionLog(BaseModel):
    id: int
    time_spent_alone: float
    stage_fear: str
    social_event_attendance: float
    going_outside: float
    drained_after_socializing: str
    friends_circle_size: float
    post_frequency: float
    predicted_personality: PersonalityEnum

    class Config:
        orm_mode = True

class PredictionResponse(BaseModel):
    personality: PersonalityEnum

class HistoryResponse(BaseModel):
    history: List[PredictionLog]