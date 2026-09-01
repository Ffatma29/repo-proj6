import { useEffect, useState } from "react";

import ThreatStats from "../components/ThreatStats";
import ThreatTable from "../components/ThreatTable";
import DetectionForm from "../components/DetectionForm";
import RiskBadge from "../components/RiskBadge";

import {
  getThreats,
  getThreatStats,
  connectThreatWebSocket,
} from "../services/threatApi";

function Dashboard() {
  const [threats, setThreats] = useState([]);
  const [stats, setStats] = useState(null);
  const [latestThreat, setLatestThreat] = useState(null);

  const loadDashboard = async () => {
    try {
      const [threatData, statsData] = await Promise.all([
        getThreats(),
        getThreatStats(),
      ]);

      setThreats(threatData.threats || []);
      setStats(statsData);

      if (threatData.threats?.length) {
        setLatestThreat(
          threatData.threats[threatData.threats.length - 1]
        );
      }
    } catch (error) {
      console.error("Failed to load dashboard:", error);
    }
  };

  useEffect(() => {
    loadDashboard();

    const socket = connectThreatWebSocket((newThreat) => {
      setLatestThreat(newThreat);

      setThreats((currentThreats) => [
        ...currentThreats,
        newThreat,
      ]);

      loadDashboard();
    });

    return () => {
      socket.close();
    };
  }, []);

  const handleDetected = (result) => {
    setLatestThreat(result);
    loadDashboard();
  };

  return (
    <div className="dashboard">
      <header>
        <h1>Threat Intelligence Dashboard</h1>
        <p>AI-powered Network Threat Detection</p>
      </header>

      <ThreatStats stats={stats} />

      <DetectionForm onDetected={handleDetected} />

      {latestThreat && (
        <div className="alert-panel">
          <h2>Latest Detection</h2>

          <p>
            <strong>{latestThreat.classification}</strong>
          </p>

          <p>Status: {latestThreat.status}</p>

          <p>
            Risk:{" "}
            <RiskBadge risk={latestThreat.risk_level} />
          </p>

          <p>
            Anomaly Score: {latestThreat.anomaly_score}
          </p>

          <p>
            Rule Based Detection:{" "}
            {latestThreat.rule_based_detection ? "Yes" : "No"}
          </p>

          {latestThreat.explanation && (
            <div className="ai-explanation">
              <h3>AI Security Analysis</h3>
              <p>{latestThreat.explanation}</p>
            </div>
          )}
        </div>
      )}

      <ThreatTable threats={threats} />
    </div>
  );
}

export default Dashboard;
