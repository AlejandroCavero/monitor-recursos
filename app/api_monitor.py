from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psutil

app_monitor = FastAPI()

app_monitor.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app_monitor.get("/monitor")

async def monitor():
    #LA CPU ESTA EN % y LA MEMORIA EN GB
    USO_CPU = psutil.cpu_percent(interval=1)
    USO_DISCO = psutil.disk_usage('/').used / (1024 ** 3)
    LIBRE_DISCO = psutil.disk_usage('/').free / (1024 ** 3)
    USO_RAM = psutil.virtual_memory().used / (1024 ** 3)
    LIBRE_RAM = psutil.virtual_memory().free / (1024 ** 3)

    return {
        "uso_cpu" : round(float(USO_CPU), 2),
        "uso_disco" : round(float(USO_DISCO), 2),
        "libre_disco" : round(float(LIBRE_DISCO), 2),
        "uso_ram" : round(float(USO_RAM), 2),
        "libre_ram" : round(float(LIBRE_RAM), 2)
        }