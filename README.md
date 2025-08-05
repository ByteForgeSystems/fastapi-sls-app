# FastAPI Serverless App

This project demonstrates a FastAPI application deployed using AWS Lambda and API Gateway via the Serverless Framework.

## Prerequisites
- Python 3.12
- Node.js & npm
- Serverless Framework (`npm install -g serverless@3.39.0`)
- AWS CLI configured with your credentials

## Local Development

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Install Node dependencies (for Serverless plugins):**
   ```bash
   npm install
   ```

3. **Run FastAPI locally:**
   ```bash
   uvicorn app.main:app --reload
   ```
   Visit: [http://localhost:8000/docs](http://localhost:8000/docs) for Swagger UI.

## Deploy to AWS Cloud

1. **Install Serverless plugins:**
   ```bash
   npm install serverless-python-requirements serverless-apigw-binary  # for binary support
   ```  

   ```bash 
   npm install serverless-python-requirements
   ```

2. **Deploy using Serverless Framework:**
   ```bash
   serverless deploy
   ```

3. **Get deployed endpoint:**
   After deployment, Serverless will output the API Gateway endpoint. Visit `<your-api-gateway-url>/docs` for Swagger UI.

## Useful Commands

- **Remove deployment from AWS:**
  ```bash
  serverless remove
  ```
- **View logs:**
  ```bash
  serverless logs -f app
  ```

## Notes
- Ensure CORS is enabled for all endpoints.
- The `/docs` and `/openapi.json` endpoints are available after deployment.
- For troubleshooting, check API Gateway settings and Lambda logs.
