# Gemstone Price Prediction

## Problem Statement

```You are hired by a company Gem Stones Co Ltd. You are provided with the dataset containing the prices and other attributes of almost 27,000 cubic gemstone. The company is earning different profits on different prize slots. You have to help the company in predicting the price for the stone on the basis of the details given in the dataset so it can distinguish between higher profitable stones and lower profitable stones so as to have a better profit share. Also, provide them with the best 5 attributes that are most important.```

## Data Dictionary

* Carat	- Carat weight of the gemstone.
* Cut - Describe the cut quality of the gemstone. Quality is increasing order Fair, Good, Very Good, Premium, Ideal.
* Color - Colour of the gemstone.With D being the best and J the worst.
* Clarity - Gemstone Clarity refers to the absence of the Inclusions and Blemishes. (In order from Best to Worst, FL = flawless, I3= level 3 inclusions) FL, IF, VVS1, VVS2, VS1, VS2, SI1, SI2, I1, I2, I3
* Depth	- The Height of a gemstone, measured from the Culet to the table, divided by its average Girdle Diameter.
* Table - The Width of the gemstone's Table expressed as a Percentage of its Average Diameter.
* Price	- the Price of the gemstone.
* X	- Length of the gemstone in mm.
* Y	- Width of the gemstone in mm.
* Z	- Height of the gemstone in mm.


### Create project template hierarchy
```bash
python template.py
```

### Setup development environment
```bash
bash init_setup.sh
```

### Acivate environment
```bash
source activate ./env
```

### Install project as local package
```bash
pip install -r requirement.txt
```

## Pipelines
### Training Pipeline
    * Data Ingestion (fetched data from source)
    * Data Transformation (Feature Engineering, Data Preprocessing)
    * Model Builing (Create a model using the processed data)

## MLFlow & DagsHub
Copy the values from DagsHub > Repo > Remote > Experiments

```bash
set MLFLOW_TRACKING_URI=<>
set MLFLOW_TRACKING_USERNAME=<>
set MLFLOW_TRACKING_PASSWORD<>
```
If the above are not set, then ML Experiments gets registered in local system else gets published to DagsHub

#### Command to train the pipeline
```bash
python src\GemstonePricePrediction\pipelines\training_pipeline.py
```

### Prediction Pipeline
    * Two types of prediction pipeline
        * Single record prediction
        * Batch prediction


## Explainer Dashboard

* Feature Importance
* Regression Stats
* Individual Predictions
* What if?
* Feature Dependence

```bash
python dashboard.py
```

## Flask App
```bash
python app.py
```

## Streamlit App
```bash
streamlit run streamlit_app.py
```

## Training Experiments - DagsHub

https://dagshub.com/abhijitpaul0212/GemstonePricePrediction


## Deployment of DockerImage on AWS
* AWS - ECR
* AWS - AppRunner

## Cloud Deployed Links
* https://gemstonepriceprediction.streamlit.app/
* https://g3smncimby.us-east-1.awsapprunner.com/


## Dataset Link
* https://www.kaggle.com/datasets/colearninglounge/gemstone-price-prediction
* https://raw.githubusercontent.com/abhijitpaul0212/DataSets/main/gemstone.csv
