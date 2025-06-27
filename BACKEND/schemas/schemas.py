from pydantic import BaseModel, field_validator
from typing import List
from enum import Enum

class YesNoEnum(str, Enum):
    yes = 'Yes'
    no = 'No'

class PersonalityEnum(str, Enum):
    introvert = 'Introvert'
    extrovert = 'Extrovert'

class PersonalityFeatures(BaseModel):
    time_spent_alone: float
    stage_fear: YesNoEnum
    social_event_attendance: float
    going_outside: float
    drained_after_socializing: YesNoEnum
    friends_circle_size: float
    post_frequency: float

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "time_spent_alone": 2.5,
                    "stage_fear": "No",
                    "social_event_attendance": 8,
                    "going_outside": 9,
                    "drained_after_socializing": "No",
                    "friends_circle_size": 15,
                    "post_frequency": 7
                },
                {
                    "time_spent_alone": 9.0,
                    "stage_fear": "Yes",
                    "social_event_attendance": 1,
                    "going_outside": 2,
                    "drained_after_socializing": "Yes",
                    "friends_circle_size": 3,
                    "post_frequency": 1
                }
            ]
        }

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

    @field_validator('stage_fear', 'drained_after_socializing', mode='before')
    @classmethod
    def format_yes_no(cls, v):
        if v == 1:
            return 'Yes'
        if v == 0:
            return 'No'
        return v
        
    class Config:
        from_attributes = True

class PredictionResponse(BaseModel):
    personality: PersonalityEnum

class HistoryResponse(BaseModel):
    history: List[PredictionLog]