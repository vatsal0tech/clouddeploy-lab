import os

from fastapi import FastAPI

app = FastAPI(
    title="CloudDeploy Lab API",
    description="A CI/CD portfolio application",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "CloudDeploy Lab is running",
        "environment": os.getenv("APP_ENV", "development"),
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/version")
def version():
    return {"version": app.version}
