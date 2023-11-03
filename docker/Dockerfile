ARG INSTALL_PYTHON_VERSION
FROM python:${INSTALL_PYTHON_VERSION}-slim-bookworm
ARG MLFLOW_VERSION

# Install python packages
COPY docker/requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt \
    pip install --no-cache mlflow==$MLFLOW_VERSION

# ENTRYPOINT ["mlflow", "server"]