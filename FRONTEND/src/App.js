import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [response, setResponse] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setResponse(null);
    setError(null);
  };

  const handleUpload = async () => {
    if (!file) {
      setError("Please select a CSV file first.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);

      const res = await axios.post(
        "http://localhost:8000/api/upload-csv/",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      setResponse(res.data);
      setError(null);

    } catch (err) {
      setError(
        err.response?.data?.error ||
        "Server not reachable. Is Django running?"
      );
      setResponse(null);

    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page">
      <div className="card">
        <h2>📤 Equipment CSV Upload</h2>
        <p className="subtitle">
          Upload your CSV file to analyze equipment data
        </p>

        <input
          type="file"
          accept=".csv"
          onChange={handleFileChange}
        />

        <button
          type="button"
          onClick={handleUpload}
          disabled={loading}
        >
          {loading ? "Uploading..." : "Upload CSV"}
        </button>

        {error && <p className="error">{error}</p>}
      </div>

      {response && (
        <div className="card">
          <h3>✅ Upload Summary</h3>
          <p>
            Total Equipment:{" "}
            <strong>{response.total_equipment}</strong>
          </p>

          <table>
            <thead>
              <tr>
                <th>Flowrate</th>
                <th>Pressure</th>
                <th>Temperature</th>
                <th>Type</th>
              </tr>
            </thead>
            <tbody>
              {response.summary.map((item, index) => (
                <tr key={index}>
                  <td>{item.Flowrate}</td>
                  <td>{item.Pressure}</td>
                  <td>{item.Temperature}</td>
                  <td>{item.Type}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default App;