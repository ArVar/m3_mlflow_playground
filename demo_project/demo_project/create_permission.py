from mlflow.server.auth.client import AuthServiceClient
from demo_project.config import settings

client = AuthServiceClient("http://admin:password@localhost:5000/")

client.create_experiment_permission("0", "newuser", "MANAGE")
ep = client.get_experiment_permission("0", "newuser")

print(f"experiment_id: {ep.experiment_id}")
print(f"user_id: {ep.user_id}")
print(f"permission: {ep.permission}")
