# Monitor-recursos hecho por Alejandro Jiménez
La app es un dashboard que muestra el uso de CPU, RAM y memoria de la máquina en la que se tenga corriendo la API, estos datos se muestran en un dashboard en tiempo real con la posibilidad de mandar alertas por telegram si se dan ciertos momentos en el sistema.

Está hecho con HTML, CSS, JavaScript y Python con FastAPI


Para empezar a usarlo lo primero es crear un venv de Pyhton, en él, debemos de descargar los siguiente paquetes:

Crear venv de Python
```
python -m venv /path/to/new/virtual/environment
```
```
.\.venv\Scripts\activate
pip install fastapi uvicorn psutil
```

Ahora para correrlo hacemos el siguiente comando:
```
uvicorn nombre_fichero_api:nombre_app --reload
```

En mi caso sería así 

```
cd app
uvicorn api_monitor:app_monitor --reload
```