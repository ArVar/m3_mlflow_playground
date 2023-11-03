from mlflow.server.auth.client import AuthServiceClient
from demo_project.config import settings

client = AuthServiceClient(
    f"http://{settings.MLFLOW_ADMIN_USER}:"
    f"{settings.MLFLOW_ADMIN_PASSWORD.get_secret_value()}@"
    "localhost:5000/"
)
# client.delete_user("newuser")
client.create_user("newuser", "newpassword")

user = client.get_user("newuser")
print(f"User name: {user.username}")
