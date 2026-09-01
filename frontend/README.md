# Threat Intelligence Dashboard

An AI-powered network threat detection dashboard built with **FastAPI**, **React**, **Machine Learning**, **CrewAI**, and **WebSockets**.

## Project Overview

This project detects suspicious network activity using a combination of:

* Machine Learning anomaly detection using Isolation Forest
* Rule-based threat detection
* Risk-level assessment
* CrewAI agents for AI-powered threat analysis and reporting
* FastAPI backend
* React + Vite frontend
* WebSocket communication for real-time threat updates

The dashboard allows users to submit network activity and view the detected classification, status, anomaly score, risk level, and rule-based detection result.

## Project Structure

```text
repo-proj6/
├── backend/
│   ├── agents/
│   │   ├── threat_agent.py
│   │   └── threat_workflow.py
│   ├── services/
│   │   ├── detection_service.py
│   │   ├── feature_engineering.py
│   │   ├── prediction_service.py
│   │   ├── risk_service.py
│   │   ├── risk_services.py
│   │   └── rule_detector.py
│   ├── data/
│   ├── models/
│   ├── main.py
│   ├── train_model.py
│   ├── evaluate_model.py
│   ├── test_risk.py
│   └── test_websocket.py
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── services/
│   ├── package.json
│   └── vite.config.js
│
├── requirements.txt
└── README.md
```

## Technologies

### Backend

* Python 3.12
* FastAPI
* Uvicorn
* Pydantic
* Scikit-learn
* Joblib
* CrewAI

### Frontend

* React
* Vite
* Axios
* JavaScript
* CSS

## Detection Pipeline

The detection process follows these steps:

1. The user submits network activity through the dashboard.
2. The React frontend sends the data to the FastAPI backend.
3. The backend processes the network features.
4. The machine-learning model calculates an anomaly score.
5. Rule-based detection checks for suspicious behavior.
6. The system determines the threat classification and risk level.
7. If an attack is detected, CrewAI analyzes the event.
8. CrewAI produces:

   * Threat analysis
   * Risk assessment
   * Security report
9. The result is stored in threat history.
10. The dashboard updates the statistics and latest detection.
11. WebSockets provide real-time threat updates.

## Risk Levels

Risk levels are determined from the anomaly score:

| Anomaly Score | Risk Level |
| ------------- | ---------- |
| Score >= 0    | Normal     |
| -0.05         | Low        |
| -0.20         | Medium     |
| -0.40         | High       |
| -0.70         | Critical   |

## Running the Backend

Go to the backend directory:

```bash
cd backend
```

Activate the Python virtual environment:

```bash
source venv312/bin/activate
```

Start the FastAPI server:

```bash
python -m uvicorn main:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

## Running the Frontend

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

The frontend will normally run at:

```text
http://localhost:5173
```

## Testing Threat Detection

Open the dashboard and use **Test Threat Detection**.

For a suspicious activity test, use for example:

```text
Failed Login Attempts: 10
Request Count: 100
```

Then click:

```text
Detect Threat
```

A suspicious event should produce a result similar to:

```text
Classification: Suspicious Activity
Status: Attack
Risk: Medium / High
Rule Based Detection: Yes
```

## Testing Risk Assessment

Run:

```bash
cd backend
source venv312/bin/activate
python test_risk.py
```

Expected results include:

```text
Score: 0.1 -> Risk: Normal
Score: -0.05 -> Risk: Low
Score: -0.2 -> Risk: Medium
Score: -0.4 -> Risk: High
Score: -0.7 -> Risk: Critical
```

## Testing WebSockets

The project provides a WebSocket endpoint:

```text
ws://127.0.0.1:8000/ws/threats
```

Run:

```bash
python test_websocket.py
```

The WebSocket is also used by the dashboard for real-time threat updates.

## API Endpoints

### Health Check

```http
GET /health
```

### Detect Threat

```http
POST /api/detect
```

### Get Threat History

```http
GET /api/threats
```

### Get Threat Statistics

```http
GET /api/threats/stats
```

### Prediction

```http
POST /predict
```

### WebSocket

```text
/ws/threats
```

## Environment Variables

Sensitive configuration such as API keys should be stored in:

```text
backend/.env
```

The `.env` file should **not** be committed to Git.

## Security

The project combines machine-learning anomaly detection with rule-based detection to improve identification of suspicious network behavior.

CrewAI is used to provide human-readable explanations and recommended follow-up actions for detected attacks.

## Project Status

The core system has been implemented and tested:

* FastAPI backend: Working
* React dashboard: Working
* Threat detection API: Working
* Machine-learning detection: Working
* Risk assessment: Working
* Rule-based detection: Working
* CrewAI threat analysis: Working
* WebSocket endpoint: Working
* Frontend dashboard: Working
* Threat history and statistics: Working
