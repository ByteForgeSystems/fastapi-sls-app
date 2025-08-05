
# --------------------
# Imports
# --------------------
import json
import os
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import HTMLResponse, JSONResponse

# --------------------
# Configuration
# --------------------
STAGE = os.environ.get('STAGE', None)
openapi_prefix = "/" if not STAGE else f"/{STAGE}"
print(f"OpenAPI prefix: {openapi_prefix}")

# --------------------
# App Setup
# --------------------
app = FastAPI(docs_url=None, openapi_prefix=openapi_prefix)

# --------------------
# Middleware
# --------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------
# Endpoints
# --------------------
@app.get("/hello")
def hello():
    """
    Returns a greeting message from FastAPI running on Serverless.
    """
    return {"message": "Hello from FastAPI + Serverless!"}

@app.get("/", response_class=HTMLResponse)
async def root():
    """
    Root endpoint with welcome message and link to Swagger UI.
    """
    return """
    <html>
        <head>
            <title>FastAPI + Serverless</title>
        </head>
        <body>
            <h1>Welcome to FastAPI + Serverless!</h1>
            <p>Visit <a href="/docs">API Documentation</a></p>
        </body>
    </html>
    """

@app.get("/health")
def health_check():
    """
    Health check endpoint. Returns service health status.
    """
    return {"status": "healthy"}

@app.get("/ping")
def ping():
    """
    Simple endpoint to check if the service is running. Returns 'pong'.
    """
    return {"message": "pong"}

@app.get("/status")
def status():
    """
    Endpoint to check the status of the service and current stage.
    """
    return {"status": "running", "stage": STAGE if STAGE else "development"}

@app.get("/info")
def info():
    """
    Endpoint to get information about the service, including stage and version.
    """
    return {
        "service": "FastAPI + Serverless",
        "stage": STAGE if STAGE else "development",
        "version": "1.0.0"
    }

# --------------------
# Documentation Endpoints
# --------------------
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html(request: Request):
    """
    Custom Swagger UI documentation endpoint.
    """
    print(f"Request path: {request.url.path}")
    print(f"OpenAPI prefix: {openapi_prefix}")
    openapi_url = f"/{STAGE}/openapi.json" if STAGE else "/openapi.json"
    return get_swagger_ui_html(
        openapi_url=openapi_url,
        title="FastAPI + Serverless Docs",
        swagger_ui_parameters={"defaultModelsExpandDepth": -1},
    )

@app.get("/openapi.json", include_in_schema=False)
async def get_openapi_json():
    """
    Returns the OpenAPI schema in JSON format for Swagger UI and other tools.
    """
    openapi = app.openapi()
    return JSONResponse(openapi, headers={
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, OPTIONS",
        "Access-Control-Allow-Headers": "*"
    })

@app.get("/openapi.yaml", include_in_schema=False)
async def get_openapi_yaml():
    """
    Returns the OpenAPI schema in YAML format for documentation and integrations.
    """
    openapi_json = app.openapi()
    return Response(
        content=json.dumps(openapi_json),
        media_type="application/x-yaml",
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, OPTIONS",
            "Access-Control-Allow-Headers": "*"
        }
    )

@app.get("/health")
def health_check():
    """
    Health check endpoint. Returns service health status.
    """
    return {"status": "healthy"}

@app.get("/ping")
def ping():
    """
    Simple endpoint to check if the service is running. Returns 'pong'.
    """
    return {"message": "pong"}

@app.get("/status")
def status():
    """
    Endpoint to check the status of the service and current stage.
    """
    return {"status": "running", "stage": STAGE if STAGE else "development"}

@app.get("/info")
def info():
    """
    Endpoint to get information about the service, including stage and version.
    """
    return {
        "service": "FastAPI + Serverless",
        "stage": STAGE if STAGE else "development",
        "version": "1.0.0"
    }

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html(request: Request):
    """
    Custom Swagger UI documentation endpoint.
    """
    print(f"Request path: {request.url.path}")
    print(f"OpenAPI prefix: {openapi_prefix}")
    # Use the openapi_prefix to generate the correct URL for OpenAPI schema
    # Set openapi_url to include stage if present
    openapi_url = f"/{STAGE}/openapi.json" if STAGE else "/openapi.json"
    return get_swagger_ui_html(
        openapi_url=openapi_url,
        title="FastAPI + Serverless Docs",
        swagger_ui_parameters={"defaultModelsExpandDepth": -1},
    )

@app.get("/openapi.json", include_in_schema=False)
async def get_openapi_json():
    """
    Returns the OpenAPI schema in JSON format for Swagger UI and other tools.
    """
    from fastapi.responses import JSONResponse
    openapi = app.openapi()
    return JSONResponse(openapi, headers={
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, OPTIONS",
        "Access-Control-Allow-Headers": "*"
    })

@app.get("/openapi.yaml", include_in_schema=False)
async def get_openapi_yaml():
    """
    Returns the OpenAPI schema in YAML format for documentation and integrations.
    """
    openapi_json = app.openapi()
    return Response(
        content=json.dumps(openapi_json),
        media_type="application/x-yaml",
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, OPTIONS",
            "Access-Control-Allow-Headers": "*"
        }
    )


