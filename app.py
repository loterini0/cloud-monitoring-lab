from flask import Flask, jsonify
import psutil
import platform
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Cloud Monitoring Lab</h1>
    <p>API de monitoreo funcionando correctamente.</p>
    <ul>
        <li><a href="/health">Estado del servidor</a></li>
        <li><a href="/metrics">Metricas del servidor</a></li>
    </ul>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "server": platform.node(),
        "timestamp": datetime.now().isoformat()
    })

@app.route("/metrics")
def metrics():
    return jsonify({
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "memory_available_mb": round(
            psutil.virtual_memory().available / 1024 / 1024, 2
        ),
        "disk_percent": psutil.disk_usage("/").percent,
        "platform": platform.system(),
        "python_version": platform.python_version()
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
