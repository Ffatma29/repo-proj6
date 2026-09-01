import RiskBadge from "./RiskBadge";

function ThreatTable({ threats }) {
  return (
    <div className="table-container">
      <h2>Threat History</h2>

      {threats.length === 0 ? (
        <p>No threats detected yet.</p>
      ) : (
        <table>
          <thead>
            <tr>
              <th>Classification</th>
              <th>Status</th>
              <th>Anomaly Score</th>
              <th>Risk</th>
              <th>Rule Based</th>
            </tr>
          </thead>

          <tbody>
            {threats.map((threat, index) => (
              <tr key={index}>
                <td>{threat.classification}</td>
                <td>{threat.status}</td>
                <td>{threat.anomaly_score}</td>
                <td>
                  <RiskBadge risk={threat.risk_level} />
                </td>
                <td>
                  {threat.rule_based_detection ? "Yes" : "No"}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default ThreatTable;
