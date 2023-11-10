# app.py

from flask import Flask, request, render_template, jsonify
from src.GemstonePricePrediction.pipelines.prediction_pipeline import PredictPipeline, CustomData
from src.GemstonePricePrediction.components.model_trainer import ModelTrainer

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
def predict_datapoint():
    """
    Prediction method
    """
    if request.method == "GET":
        return render_template("form.html")
    
    else:
        data = CustomData(
            
            carat=float(request.form.get('carat')),
            depth=float(request.form.get('depth')),
            table=float(request.form.get('table')),
            x=float(request.form.get('x')),
            y=float(request.form.get('y')),
            z=float(request.form.get('z')),
            cut=request.form.get('cut'),
            color=request.form.get('color'),
            clarity=request.form.get('clarity')
        )
        final_data = data.get_data_as_dataframe()
        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(final_data)
        result = round(pred[0], 2)

        return render_template("result.html", final_result=result, model_score=round(ModelTrainer().show_model_score()*100, 2))
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
