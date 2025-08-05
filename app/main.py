import json
import os
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware

# Application configuration
STAGE = os.environ.get('STAGE', None)

# FastAPI configuration
openapi_prefix = "/" if not STAGE else f"/{STAGE}"

print(f"OpenAPI prefix: {openapi_prefix}")



app = FastAPI(docs_url=None)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/hello")
def hello():
    return {"message": "Hello from FastAPI + Serverless!"}



from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import HTMLResponse

@app.get("/", response_class=HTMLResponse)
async def root():
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
    return {"status": "healthy"}

@app.get("/ping")
def ping():
    """
    Simple endpoint to check if the service is running.
    """
    return {"message": "pong"}

@app.get("/status") 
def status():
    """
    Endpoint to check the status of the service.
    """
    return {"status": "running", "stage": STAGE if STAGE else "development"}

@app.get("/info")
def info():
    """
    Endpoint to get information about the service.
    """
    return {
        "service": "FastAPI + Serverless",
        "stage": STAGE if STAGE else "development",
        "version": "1.0.0"
    }

@app.get("/docs", include_in_schema=False)
async def get_docs(request: Request):
    """
    Custom documentation endpoint.
    """
    print(f"Request path: {request.url.path}")
    print(f"OpenAPI prefix: {openapi_prefix}")
    # Use the openapi_prefix to generate the correct URL for OpenAPI schema
    return get_swagger_ui_html(
        openapi_url=openapi_prefix+"/openapi.json",
        title="FastAPI + Serverless Docs",
        swagger_ui_parameters={"defaultModelsExpandDepth": -1},
    )

@app.get("/openapi.json", include_in_schema=False)
async def get_openapi_json():
    """
    Endpoint to retrieve the OpenAPI schema in JSON format.
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
    Endpoint to retrieve the OpenAPI schema in YAML format.
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


