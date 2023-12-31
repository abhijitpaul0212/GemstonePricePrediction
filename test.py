# test.py
from src.GemstonePricePrediction.pipelines.training_pipeline import TrainingPipeline
from src.GemstonePricePrediction.pipelines.prediction_pipeline import CustomData, PredictPipeline
from src.GemstonePricePrediction.components.model_trainer import ModelTrainer


training_pipeline = TrainingPipeline()
training_pipeline.start()

model_tr = ModelTrainer()
model_tr.show_model_score()


data = CustomData(1.52, 62.2, 58.0, 7.27, 7.33, 4.55, "Premium", "F", "VS2")
final_data = data.get_data_as_dataframe()
print(final_data)

predict_pipeline = PredictPipeline()
pred = predict_pipeline.predict(final_data)
result = round(pred[0], 2)

print(result)
