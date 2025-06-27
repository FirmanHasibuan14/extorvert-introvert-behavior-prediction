import joblib
import pandas as pd
from schemas import schemas

class MLService:
    def __init__(self, model_path: str):
        try:
            self.model = joblib.load(model_path)
        except Exception as e:
            self.model = None
            print(f"Error saat memuat model: {e}")
    
    def predict(self, features: schemas.PersonalityFeatures) -> schemas.PersonalityEnum:
        if not self.model:
            return schemas.PersonalityEnum.introvert
        
        input_data = {
            "Time_spent_Alone": features.Time_spent_Alone,
            "Stage_fear": 1 if features.Stage_fear == "Yes" else 0,
            "Social_event_attendace": features.Social_event_attendance,
            "Going_outside": features.Going_outside,
            "Drained_after_socializing": 1 if features.Drained_after_socializing == "Yes" else 0,
            "Friend_circle_size": features.Friends_circle_size,
            "Post_frequency": features.Post_frequency,
        }

        data_df = pd.DataFrame([input_data])
        prediction = self.model.predict(data_df)

        return schemas.PersonalityEnum.introvert if prediction[0] == 0 else schemas.PersonalityEnum.extrovert
    
ml_service_instance = MLService(model_path="/ML/Model/introvert_vs_extrovert_behavior.pkl")