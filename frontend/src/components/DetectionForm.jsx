import { useState } from "react";
import { detectThreat } from "../services/threatApi";

function DetectionForm({ onDetected }) {
  const [failedLogins, setFailedLogins] = useState(0);
  const [count, setCount] = useState(1);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();

    setLoading(true);

    try {
      const log = {
        protocol_type: "tcp",
        service: "http",
        flag: failedLogins >= 5 ? "S0" : "SF",
        duration: failedLogins >= 5 ? 10 : 0,
        src_bytes: failedLogins >= 5 ? 5000 : 100,
        dst_bytes: 200,

        land: 0,
        wrong_fragment: 0,
        urgent: 0,
        hot: failedLogins >= 5 ? 10 : 0,

        num_failed_logins: Number(failedLogins),
        logged_in: failedLogins >= 5 ? 0 : 1,
        num_compromised: 0,
        root_shell: 0,
        su_attempted: 0,
        num_root: 0,
        num_file_creations: 0,
        num_shells: 0,
        num_access_files: 0,
        num_outbound_cmds: 0,
        is_host_login: 0,
        is_guest_login: 0,

        count: Number(count),
        srv_count: Number(count),

        serror_rate: failedLogins >= 5 ? 0.9 : 0,
        srv_serror_rate: failedLogins >= 5 ? 0.9 : 0,
        rerror_rate: 0,
        srv_rerror_rate: 0,

        same_srv_rate: failedLogins >= 5 ? 0.1 : 1,
        diff_srv_rate: failedLogins >= 5 ? 0.9 : 0,
        srv_diff_host_rate: 0,

        dst_host_count: Number(count),
        dst_host_srv_count: Number(count),

        dst_host_same_srv_rate: failedLogins >= 5 ? 0.2 : 1,
        dst_host_diff_srv_rate: failedLogins >= 5 ? 0.8 : 0,
        dst_host_same_src_port_rate: 1,
        dst_host_srv_diff_host_rate: 0,

        dst_host_serror_rate: failedLogins >= 5 ? 0.9 : 0,
        dst_host_srv_serror_rate: failedLogins >= 5 ? 0.9 : 0,
        dst_host_rerror_rate: 0,
        dst_host_srv_rerror_rate: 0,
      };

      const result = await detectThreat(log);
      onDetected(result);
    } catch (error) {
      console.error(error);
      alert("Detection request failed.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <form className="detection-form" onSubmit={handleSubmit}>
      <h2>Test Threat Detection</h2>

      <label>
        Failed Login Attempts
        <input
          type="number"
          min="0"
          value={failedLogins}
          onChange={(e) => setFailedLogins(e.target.value)}
        />
      </label>

      <label>
        Request Count
        <input
          type="number"
          min="1"
          value={count}
          onChange={(e) => setCount(e.target.value)}
        />
      </label>

      <button type="submit" disabled={loading}>
        {loading ? "Analyzing..." : "Detect Threat"}
      </button>
    </form>
  );
}

export default DetectionForm;
