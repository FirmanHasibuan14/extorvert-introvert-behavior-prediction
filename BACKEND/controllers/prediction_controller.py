from sqlalchemy.orm import Session
from services.ml_service import MLService
from schemas import schemas
from models import db_models

def create_prediction_and_log(features: schemas.PersonalityFeatures, service: MLService, db: Session):
    personality = service.predict(features)

    stage_fear_int = 1 if features.stage_fear == schemas.YesNoEnum.yes else 0
    drained_after_socializing_int = 1 if features.drained_after_socializing == schemas.YesNoEnum.yes else 0

    db_log = db_models.PredictionLog(
        time_spent_alone=features.time_spent_alone,
        stage_fear=stage_fear_int,
        social_event_attendance=features.social_event_attendance,
        going_outside=features.going_outside,
        drained_after_socializing=drained_after_socializing_int,
        friends_circle_size=features.friends_circle_size,
        post_frequency=features.post_frequency,
        predicted_personality=personality.value
    )

    db.add(db_log)
    db.commit()
    db.refresh(db_log)

    return personality

def get_all_history(db: Session, skip: int, limit: int):
    return db.query(db_models.PredictionLog).offset(skip).limit(limit).all()