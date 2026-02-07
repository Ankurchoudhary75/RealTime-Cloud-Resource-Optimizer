# Architecture Diagram Description

User / Dashboard
        |
        v
Docker Compose
        |
        v
Optimizer Service (FastAPI)
  - Metrics Collector (psutil)
  - Decision Engine
  - Scaling Controller
        |
        v
Docker Engine
  - Worker Containers (alpine)
