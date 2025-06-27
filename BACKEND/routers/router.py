from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from controllers import prediction_controller
from schemas import schemas
from database.database import get_db
from services.ml_service import MLService, get_ml_service

router = APIRouter(
    prefix="/v1",
    tags=["Predictions"]
)

@router.post("/predict", response_model=schemas.PredictionResponse)
def predict_personality(features: schemas.PersonalityFeatures, db: Session = Depends(get_db), service: MLService = Depends(get_ml_service)):
    prediction = prediction_controller.create_prediction_and_log(features=features, service=service, db=db)
    return {"personality": prediction}

@router.get("/history", response_model=schemas.HistoryResponse)
def read_history(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    history_logs = prediction_controller.get_all_history(db, skip=skip, limit=limit)
    return {"history": history_logs}