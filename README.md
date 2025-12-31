# Obesity API (Health Oracle)

Live docs: https://obesity-api-0v0o.onrender.com/docs

Description

This repository provides the Obesity prediction API and is part of the Health Oracle application. The underlying ML model has been trained, validated and deployed. Use the API to predict obesity risk (or classification) for given patient features. For exact endpoint details and field definitions, consult the live docs linked above.

Key notes

- Part of Health Oracle microservices.
- Trained and deployed ML model artifact served by this API.
- Interactive API documentation available at /docs.

Quick Start (consume the API)

- Base URL: https://obesity-api-0v0o.onrender.com
- Interactive docs: https://obesity-api-0v0o.onrender.com/docs

Example JSON request (example fields — confirm via /docs):

POST /predict
Content-Type: application/json

Request body (example):
{
  "age": 30,
  "gender": "female",
  "height_cm": 165,
  "weight_kg": 75,
  "physical_activity_level": 2,
  "diet_score": 3
}

Example JSON response (example):
{
  "prediction": "overweight",
  "probability": 0.82
}

Local development

1. Clone the repo
   git clone https://github.com/rangabharathkumar/Obesity_api.git
2. Create and activate virtualenv and install deps
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
3. Run locally (example)
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

Open http://localhost:8000/docs for the interactive docs.

Environment

- Provide model path, secrets and other config via environment variables or .env.

Testing

- Use pytest or the test suite included in the repo.

Using as reference

- Fork or clone to adapt to your datasets and models. Replace model file, adjust preprocessing, and validate end-to-end before production.

Author

Ranga Bharath Kumar — https://github.com/rangabharathkumar

Canonical docs: https://obesity-api-0v0o.onrender.com/docs
