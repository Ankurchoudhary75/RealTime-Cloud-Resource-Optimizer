# config.py

MODE = "REAL"
   # change to "REAL" when ready

MIN_REPLICAS = 1
MAX_REPLICAS = 3

SERVICE_NAME = "optimizer_worker"
WORKER_IMAGE = "alpine"
WORKER_COMMAND = "sleep 3600"
