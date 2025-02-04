import { useEffect, useState } from "react";

export default function LabourActViewer() {
  const [text, setText] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:5000/api/data") // Backend API URL
      .then((res) => res.json())
      .then((data) => setText(data.data))
      .catch((err) => console.error("Error fetching text:", err));
  }, []);

  return (
    <div className="p-8 bg-gray-900 min-h-screen text-white">
      <h1 className="text-3xl font-bold mb-6 border-b-2 pb-2">📜 Labour Act - Extracted Data</h1>
      <div className="bg-gray-800 p-6 rounded-lg shadow-lg">
        <pre className="whitespace-pre-wrap text-lg font-mono leading-relaxed">
          {text}
        </pre>
      </div>
    </div>
  );
}
