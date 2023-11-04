import os
from explainerdashboard import ExplainerDashboard

yaml_file = os.path.join('artifacts', 'dashboard.yaml')
explainer_file = os.path.join('artifacts', 'explainer.joblib')
db = ExplainerDashboard.from_config(explainer_file, yaml_file)
app = db.flask_server()


if __name__ == '__main__':
    app.run(port=8051)
