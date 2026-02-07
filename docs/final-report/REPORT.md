# Real-Time Cloud Computing Resource Optimizer

## 1. Introduction
This project implements a real-time cloud resource optimizer that monitors system metrics and automatically scales resources based on workload. The system supports both simulation and real Docker-based scaling.

## 2. Problem Statement
Static resource allocation leads to underutilization or overload. Manual scaling is slow and error-prone. An automated optimizer is required to make real-time scaling decisions.

## 3. Objectives
- Monitor CPU and memory usage in real time
- Decide scaling actions automatically
- Support safe simulation and real execution modes
- Containerize and orchestrate services using Docker and Docker Compose

## 4. System Architecture
The system consists of a FastAPI-based optimizer service, optional worker containers, and Docker-based orchestration.

## 5. Technologies Used
- Python, FastAPI
- Docker, Docker Compose
- Docker SDK for Python
- GitHub for version control

## 6. Implementation Details
- Background thread monitors metrics
- Threshold-based decision engine
- Simulation mode for safe testing
- Real mode for Docker container scaling
- Docker socket mounting for controlled orchestration

## 7. Results
The optimizer successfully created and removed Docker containers based on real-time CPU load.

## 8. Conclusion
The project demonstrates a production-style auto-scaling system with safety controls and modular design.

## 9. Future Scope
- Kubernetes Horizontal Pod Autoscaler
- Predictive scaling using ML
- Cloud provider integration (AWS/GCP)
