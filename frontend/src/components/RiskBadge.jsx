function RiskBadge({ risk }) {
  return (
    <span className={`risk-badge risk-${risk?.toLowerCase()}`}>
      {risk || "Unknown"}
    </span>
  );
}

export default RiskBadge;
