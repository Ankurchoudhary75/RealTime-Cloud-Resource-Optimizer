from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psutil
import threading
import time

from optimizer import decide_scaling
from scaler import apply_scaling
from docker_scaler import scale_real
from config import MODE

app = FastAPI(title="Real-Time Cloud Resource Optimizer")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

latest_state = {}
stop_event = threading.Event()

def auto_optimize():
    while not stop_event.is_set():
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent

        decision = decide_scaling(cpu)

        if MODE == "SIMULATION":
            replicas = apply_scaling(decision)
        else:
            replicas = scale_real(decision)

        latest_state.update({
            "mode": MODE,
            "cpu_usage_percent": cpu,
            "memory_usage_percent": memory,
            "scaling_decision": decision,
            "active_replicas": replicas
        })

        print("Optimizer State:", latest_state)
        time.sleep(5)

@app.on_event("startup")
def start_optimizer():
    threading.Thread(target=auto_optimize, daemon=True).start()

@app.on_event("shutdown")
def stop_optimizer():
    stop_event.set()

@app.get("/")
def root():
    return {"status": "Optimizer running", "mode": MODE}

@app.get("/metrics")
def metrics():
    return latest_state
