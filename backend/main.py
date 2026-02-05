from fastapi import FastAPI
import psutil
import threading
import time
from optimizer import decide_scaling

app = FastAPI(title="Real-Time Cloud Resource Optimizer")

latest_decision = {}
stop_event = threading.Event()

def auto_optimize():
    while not stop_event.is_set():
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        decision = decide_scaling(cpu)

        latest_decision.update({
            "cpu_usage_percent": cpu,
            "memory_usage_percent": memory,
            "scaling_decision": decision
        })

        print("Auto Optimization:", latest_decision)
        time.sleep(5)

@app.on_event("startup")
def start_optimizer():
    threading.Thread(target=auto_optimize, daemon=True).start()

@app.on_event("shutdown")
def stop_optimizer():
    stop_event.set()

@app.get("/")
def root():
    return {"status": "Backend is running"}

@app.get("/metrics")
def get_metrics():
    return latest_decision
