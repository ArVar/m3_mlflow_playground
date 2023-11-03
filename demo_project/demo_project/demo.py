import os
import mlflow
from mlflow.models import infer_signature
# from mlflow import environment_variables

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor

from demo_project.config import settings

os.environ["AWS_ACCESS_KEY_ID"] = settings.MINIO_ACCESS_KEY_ID.get_secret_value()
os.environ[
    "AWS_SECRET_ACCESS_KEY"
] = settings.MINIO_SECRET_ACCESS_KEY.get_secret_value()
os.environ["MLFLOW_S3_ENDPOINT_URL"] = settings.OBJECT_STORAGE_URL
os.environ["MLFLOW_TRACKING_USERNAME"] = "newuser"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "newpassword"

mlflow.set_tracking_uri("http://localhost:5000/")
mlflow.autolog()

with mlflow.start_run(run_name="Test Run") as run:
    # Load the diabetes dataset.
    db = load_diabetes()
    X_train, X_test, y_train, y_test = train_test_split(db.data, db.target)

    # Create and train models.
    rf = RandomForestRegressor(n_estimators=100, max_depth=6, max_features=3)
    rf.fit(X_train, y_train)

    # Use the model to make predictions on the test dataset.
    predictions = rf.predict(X_test)
    print(predictions)

    signature = infer_signature(X_test, predictions)
    mlflow.sklearn.log_model(rf, "model", signature=signature)

    mlflow.log_metrics({"Benutzer": 5.0, "Admin": 1.0}, step=1)
    mlflow.log_params({"Benutzer": "Zarah", "Admin": "Arthur"})

    print(f"Run ID: {run.info.run_id}")
