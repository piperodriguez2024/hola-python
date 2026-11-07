from fastapi import FastAPI
from main import saludar

app = FastAPI(
    title="Laboratorio DevOps SRE IA",
    description="API REST del laboratorio personal",
    version="0.1.0"
)


@app.get("/")
def inicio():
    return {
        "proyecto": "Laboratorio DevOps SRE IA",
        "estado": "activo",
        "version": "0.1.0"
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "hola-python-api"
    }


@app.get("/saludo/{nombre}")
def obtener_saludo(nombre: str):
    return {
        "mensaje": saludar(nombre)
    }
