# M3 MLflow Playground On-Premise Deployment using `docker compose`

If you want to deploy an MLflow playground for testing with all relevant components and a demo project, here is a suitable setup.


## Components & Services

We have 3 components here:
* MinIO S3 is used as the artifact store
* MariaDB server is used as the backend database
* MLflow server is our tracking server

The `docker-compose.yml` provides 4 services, accordingly:

| Service | Container Name | Function |
|---------|----------------|----------|
| minio | mlflow_s3 | S3 compatible object storage |
| minio-client | mlflow_mc | [MinIO client](https://min.io/docs/minio/linux/reference/minio-mc.html) runner |
| db | mlflow_db | [MariaDB](https://mariadb.com/docs/) backend database |
| mlflow | mlflow_server | Tracking server ([MLflow](https://mlflow.org/docs/latest/index.html) instance) |



## How to setup the infrastructure

1. Clone (download) this repository

    ```bash
    git clone https://github.com/arvar/m3-mlflow-playground.git
    ```

2. `cd` into the `m3-mlflow-playground` directory

3. Create an `.env` file from the provided `example.env` file

4. Fill the passwords accordingly. (Keep in mind, that the MLflow default user is `admin` and the default password is `password`.You can change it as described in the MLflow documentation.)

3. Build and run the containers with `docker compose`

    ```bash
    docker compose up -d --build
    ```

4. Access MLflow UI with http://localhost:5000

5. Access MinIO UI with http://localhost:9000


## Demo Project

The demo project contains a simple scikit-learn use-case.
It was initialized with [poetry](https://python-poetry.org) and uses it as dependency management (and packaging) tool.

### Installation of the environment
*You will need to install [conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) and [poetry](https://python-poetry.org/docs/) if not already available on your system.*

Make sure your desired python environment is available and poetry is installed (see [here](https://python-poetry.org/docs/#installation)). If you don't have an environment you can create it by using

```bash
conda env create -f base_env.yml
```

from within the repo root folder where the `base_env.yml` is provided.

You can check the path to the environment by using:

```bash
conda env list
```

The path to your binary would be the output of the above command plus `<your_env_path>\python.exe` (Windows) or `<your_env_path>\bin\python` (Linux).

Now you can do the following steps:

1. `cd` into the `demo_project` directory
2. Tell poetry which python to use:

    ```bash
    poetry env use <path_to_your_python_binary>  # e.g. %USERPROFILE%\.conda\envs\m3-mlflow-playground\python.exe
    ```

    You can check the used Python environment by typing:
    
    ```bash
    poetry env info
    ```
3. Install the project environment:
    ```bash
    poetry install
    ```

4. Now you can use the created environment in your IDE and run the scripts.

Happy testing & coding! 😊

### Example

Everything has to be set up like described above.
Now you can:

1. Create a user by running `create_user.py`.

2. Give the user `MANAGE` permissions on the experiment with ID `0` (Default Experiment).

3. Run the demo training with `demo.py`


## Sources

* https://github.com/sachua/mlflow-docker-compose

* https://github.com/Toumash/mlflow-docker