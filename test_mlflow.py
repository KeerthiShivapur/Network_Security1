import os

# MLflow credentials
os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/keerthishivapur5/Network_Security.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"] = "keerthishivapur5"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "bef63fa5da60c5a096e430f95d891778d6043f2d"

# Initialize DagsHub + MLflow
import dagshub
dagshub.init(
    repo_owner='keerthishivapur5',
    repo_name='Network_Security',
    mlflow=True
)

import mlflow

# Test run
with mlflow.start_run():
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_metric("accuracy", 0.95)
