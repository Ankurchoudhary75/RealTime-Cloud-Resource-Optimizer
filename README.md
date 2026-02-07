# Real-Time Cloud Computing Resource Optimizer 🚀

A production-style cloud resource optimizer that monitors system resources in real time and automatically scales Docker containers based on workload.  
The system supports both **simulation mode** (safe testing) and **real Docker-based auto-scaling**.

---

## 📌 Key Features

- 🔍 Real-time CPU & memory monitoring
- 🧠 Intelligent scaling decision engine
- 🔁 Background auto-optimization loop
- 🐳 Real Docker container scaling using Docker SDK
- 🧪 Simulation mode for safe demos
- 📦 Dockerized backend
- 🧩 Multi-service orchestration using Docker Compose
- 🔒 Safe scaling limits (min/max replicas)

---

## 🏗️ System Architecture

User / Dashboard
|
v
Optimizer Service (FastAPI)

Metrics Collector

Decision Engine

Scaling Controller
|
v
Docker Engine

Worker Containers

---

## ⚙️ Technologies Used

- **Python**
- **FastAPI**
- **Docker & Docker Compose**
- **Docker SDK for Python**
- **psutil**
- **Git & GitHub**

---

## 🚀 How It Works

1. The optimizer continuously monitors CPU and memory usage.
2. A decision engine determines whether to scale up, scale down, or stay stable.
3. In **SIMULATION mode**, scaling is logical (no containers created).
4. In **REAL mode**, Docker containers are dynamically created or removed.
5. Docker Compose orchestrates the optimizer service.

---

## ▶️ Running the Project

### 🔹 Prerequisites
- Docker Desktop
- Python 3.9+
- Git

---

### 🔹 Run using Docker Compose (Recommended)

```bash
docker compose up --build

# How to Access:


API: http://localhost:8000

Docs: http://localhost:8000/docs

Metrics: http://localhost:8000/metrics

#How to Stop:
docker compose down

🧪 Simulation vs Real Mode

The project supports two modes via configuration:
MODE = "SIMULATION"  # Safe mode
MODE = "REAL"        # Real Docker scaling

📈 Results

Successfully demonstrated real-time auto-scaling

Docker containers were dynamically created and removed based on CPU load

Clean startup and teardown using Docker Compose

🔮 Future Enhancements

Kubernetes (HPA) integration

Predictive scaling using Machine Learning

Cloud provider support (AWS/GCP)

Web-based monitoring dashboard

dashboard

👨‍💻 Author

Ankur Choudhary
GitHub: https://github.com/Ankurchoudhary75