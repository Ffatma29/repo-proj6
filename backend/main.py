from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from services.prediction_service import predict_threat
from services.detection_service import detect_threat
from agents.threat_workflow import analyze_threat


app = FastAPI(
    title="Threat Intelligence Dashboard",
    description="AI-powered network threat detection API",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


threat_history = []
connected_clients = []


class NetworkLog(BaseModel):
    duration: int = 0
    protocol_type: str = "tcp"
    service: str = "http"
    flag: str = "SF"
    src_bytes: int = 0
    dst_bytes: int = 0
    land: int = 0
    wrong_fragment: int = 0
    urgent: int = 0
    hot: int = 0
    num_failed_logins: int = 0
    logged_in: int = 0
    num_compromised: int = 0
    root_shell: int = 0
    su_attempted: int = 0
    num_root: int = 0
    num_file_creations: int = 0
    num_shells: int = 0
    num_access_files: int = 0
    num_outbound_cmds: int = 0
    is_host_login: int = 0
    is_guest_login: int = 0
    count: int = 0
    srv_count: int = 0
    serror_rate: float = 0.0
    srv_serror_rate: float = 0.0
    rerror_rate: float = 0.0
    srv_rerror_rate: float = 0.0
    same_srv_rate: float = 0.0
    diff_srv_rate: float = 0.0
    srv_diff_host_rate: float = 0.0
    dst_host_count: int = 0
    dst_host_srv_count: int = 0
    dst_host_same_srv_rate: float = 0.0
    dst_host_diff_srv_rate: float = 0.0
    dst_host_same_src_port_rate: float = 0.0
    dst_host_srv_diff_host_rate: float = 0.0
    dst_host_serror_rate: float = 0.0
    dst_host_srv_serror_rate: float = 0.0
    dst_host_rerror_rate: float = 0.0
    dst_host_srv_rerror_rate: float = 0.0


@app.get("/")
def root():
    return {
        "message": "Threat Intelligence API is running",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }


async def broadcast_threat(result):
    disconnected = []

    for websocket in connected_clients:
        try:
            await websocket.send_json(result)
        except Exception:
            disconnected.append(websocket)

    for websocket in disconnected:
        if websocket in connected_clients:
            connected_clients.remove(websocket)


@app.post("/api/detect")
async def detect(log: NetworkLog):
    data = log.model_dump()

    result = detect_threat(data)

    # Add CrewAI explanation only for suspicious events
    if result["status"] == "Attack":
        try:
            result["explanation"] = analyze_threat(result)
        except Exception as error:
            result["explanation"] = (
                f"CrewAI analysis unavailable: {error}"
            )

    threat_history.append(result)

    await broadcast_threat(result)

    return result


@app.get("/api/threats")
def get_threats():
    return {
        "threats": threat_history,
    }


@app.get("/api/threats/stats")
def get_threat_stats():
    total = len(threat_history)

    risk_counts = {
        "Normal": 0,
        "Low": 0,
        "Medium": 0,
        "High": 0,
        "Critical": 0,
    }

    for threat in threat_history:
        risk = threat.get("risk_level")

        if risk in risk_counts:
            risk_counts[risk] += 1

    return {
        "total": total,
        "by_risk_level": risk_counts,
    }


@app.post("/predict")
def predict(log: NetworkLog):
    data = log.model_dump()
    return predict_threat(data)


@app.websocket("/ws/threats")
async def websocket_threats(websocket: WebSocket):
    await websocket.accept()
    connected_clients.append(websocket)

    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        if websocket in connected_clients:
            connected_clients.remove(websocket)