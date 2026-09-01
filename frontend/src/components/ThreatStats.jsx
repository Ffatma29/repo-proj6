function ThreatStats({ stats }) {
  const risks = stats?.by_risk_level || {};

  return (
    <div className="stats-grid">
      <div className="stat-card">
        <h3>Total</h3>
        <strong>{stats?.total || 0}</strong>
      </div>

      <div className="stat-card">
        <h3>Normal</h3>
        <strong>{risks.Normal || 0}</strong>
      </div>

      <div className="stat-card">
        <h3>Low</h3>
        <strong>{risks.Low || 0}</strong>
      </div>

      <div className="stat-card">
        <h3>Medium</h3>
        <strong>{risks.Medium || 0}</strong>
      </div>

      <div className="stat-card">
        <h3>High</h3>
        <strong>{risks.High || 0}</strong>
      </div>

      <div className="stat-card">
        <h3>Critical</h3>
        <strong>{risks.Critical || 0}</strong>
      </div>
    </div>
  );
}

export default ThreatStats;
