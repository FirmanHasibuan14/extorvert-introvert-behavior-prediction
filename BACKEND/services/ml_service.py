import joblib
import pandas as pd
from schemas import schemas
import os

class MLService:
    def __init__(self, model_path: str):
        try:
            self.model = joblib.load(model_path)
            print(f"Model berhasil dimuat dari: {model_path}")
        except FileNotFoundError:
            self.model = None
            print(f"Error: Model tidak dapat ditemukan di path '{model_path}'. Fungsi prediksi tidak akan bekerja.")
        except Exception as e:
            self.model = None
            print(f"Error saat memuat model: {e}")
    
    def predict(self, features: schemas.PersonalityFeatures) -> schemas.PersonalityEnum:
        if not self.model:
            raise RuntimeError("Model ML tidak berhasil dimuat, prediksi tidak dapat dilakukan.")
        
        input_data = {
            "Time_spent_Alone": features.time_spent_alone,
            "Stage_fear": 1 if features.stage_fear == schemas.YesNoEnum.yes else 0,
            "Social_event_attendance": features.social_event_attendance, 
            "Going_outside": features.going_outside,
            "Drained_after_socializing": 1 if features.drained_after_socializing == schemas.YesNoEnum.yes else 0,
            "Friends_circle_size": features.friends_circle_size, 
            "Post_frequency": features.post_frequency,
        }

        data_df = pd.DataFrame([input_data])
        prediction = self.model.predict(data_df)

        return schemas.PersonalityEnum.introvert if prediction[0] == 0 else schemas.PersonalityEnum.extrovert

ml_service = MLService(model_path='../ML/Model/introvert_vs_extrovert_behavior.pkl')

def get_ml_service():
    return ml_service