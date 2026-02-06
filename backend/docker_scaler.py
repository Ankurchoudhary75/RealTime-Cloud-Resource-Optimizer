import docker
from config import SERVICE_NAME, WORKER_IMAGE, WORKER_COMMAND, MIN_REPLICAS, MAX_REPLICAS

client = docker.from_env()

def list_workers():
    return client.containers.list(filters={"name": SERVICE_NAME})

def scale_real(decision: str) -> int:
    containers = list_workers()
    count = len(containers)

    # 🔥 BOOTSTRAP: ensure minimum container exists
    if count == 0 and decision in ["SCALE_UP", "STABLE"]:
        client.containers.run(
            WORKER_IMAGE,
            command=WORKER_COMMAND,
            name=f"{SERVICE_NAME}_1",
            detach=True
        )
        return 1

    if decision == "SCALE_UP" and count < MAX_REPLICAS:
        client.containers.run(
            WORKER_IMAGE,
            command=WORKER_COMMAND,
            name=f"{SERVICE_NAME}_{count+1}",
            detach=True
        )

    elif decision == "SCALE_DOWN" and count > MIN_REPLICAS:
        containers[-1].stop()
        containers[-1].remove()

    return len(list_workers())
