import { useState } from "react";
import "./App.css";

function App() {
  const [url, setUrl] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const analyzeWebsite = async () => {
    if (!url) {
      alert("Please enter a URL");
      return;
    }

    setLoading(true);

    try {
      const response = await fetch("http://127.0.0.1:5000/analyze", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ url }),
      });

      const data = await response.json();
      setResult(data);
    } catch (error) {
      setResult({ error: "Unable to connect to backend." });
    }

    setLoading(false);
  };

  return (
    <div className="container">
      <h1>Page Pulse</h1>

      <input
        type="text"
        placeholder="https://example.com"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        style={{
          width: "100%",
          padding: "12px",
          marginBottom: "10px",
        }}
      />

      <button onClick={analyzeWebsite}>
        {loading ? "Analyzing..." : "Analyze Website"}
      </button>

      {result && (
  <div className="report">
    {result.error ? (
      <p className="error"></p>
    ) : (
      <>
        <h2>Analysis Report</h2>

        <p><strong>Page Title:</strong> {result.page_title}</p>

        <p><strong>HTTP Status:</strong> {result.http_status}</p>

        <p><strong>Response Time:</strong> {result.response_time_ms} ms</p>

        <p><strong>Meta Description:</strong> {result.meta_description}</p>

        <p><strong>H1 Count:</strong> {result.h1_count}</p>

        <p><strong>Images Missing Alt:</strong> {result.images_missing_alt}</p>

        <p><strong>Word Count:</strong> {result.word_count}</p>
      </>
    )}
  </div>
)}

      <footer style={{ marginTop: "40px" }}>
  <a
    href="https://digitalheroesco.com"
    target="_blank"
    rel="noopener noreferrer"
  >
    Built for Digital Heroes Training Task
  </a>
</footer>
    </div>
  );
}

export default App;