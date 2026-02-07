Q1. What does your project do?
It monitors system resources in real time and automatically scales containers based on load.

Q2. Why Docker?
Docker provides lightweight, isolated environments suitable for dynamic scaling.

Q3. What is simulation mode?
A safe mode where scaling decisions are applied logically without creating containers.

Q4. How did you perform real scaling?
Using Docker SDK with controlled access to the Docker socket.

Q5. Why Docker Compose?
To orchestrate services with a single command and manage lifecycle cleanly.

Q6. Is mounting Docker socket safe?
Not for production, but acceptable for local demos and learning projects.

Q7. Future improvements?
Kubernetes HPA and predictive scaling.
