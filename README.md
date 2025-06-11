This project is an end-to-end machine learning pipeline built to detect phishing or malicious network activity from raw network traffic data. It is designed with modularity, scalability, and production-readiness in mind — covering the complete lifecycle from data ingestion to deployment.

## Project Structure
```
.
├── app.py                 # API endpoint using FastAPI
├── Dockerfile             # Docker setup
├── networksecurity/       # Core ML pipeline code
│   ├── components/        # Data ingestion, transformation, validation, etc.
│   ├── entity/            # Data and config entities
│   ├── exception/         # Custom error handling
│   ├── logging/           # Logging logic
│   ├── pipeline/          # Training & batch prediction pipelines
│   ├── constant/          # Schema and path constants
│   └── utils/             # Helper utilities
├── Artifacts/             # Auto-generated outputs (models, reports)
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
```