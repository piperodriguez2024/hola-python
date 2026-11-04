# Laboratorio DevOps, SRE e Inteligencia Artificial

![Python CI](https://github.com/piperodriguez2024/hola-python/actions/workflows/python-ci.yml/badge.svg)

Laboratorio personal de ingenieria de software,
DevOps, DevSecOps, SRE e Inteligencia Artificial.

Desarrollado en Steam Deck LCD utilizando
SteamOS, Distrobox, Ubuntu 24.04 y Python.

## Objetivo

Construir progresivamente una plataforma
de desarrollo y operaciones que integre:

- Desarrollo de software con Python
- Git y control de versiones
- Integracion y entrega continua
- Seguridad automatizada (DevSecOps)
- APIs y contenedores
- Kubernetes y GitOps
- Observabilidad y confiabilidad
- Inteligencia Artificial aplicada a SRE

## Arquitectura actual

Steam Deck + Ubuntu (Distrobox)
          |
          v
    Codigo Python
          |
          v
    Git + GitHub
          |
          v
    GitHub Actions
          |
          v
    Pruebas unittest
          |
          v
    Resultado CI

## Tecnologias

| Tecnologia | Uso |
|---|---|
| SteamOS | Sistema anfitrion |
| Distrobox | Entorno Linux aislado |
| Ubuntu 24.04 | Entorno de desarrollo |
| Python 3 | Desarrollo de aplicaciones |
| Git | Control de versiones |
| GitHub | Repositorio de codigo |
| GitHub Actions | Integracion continua |
| unittest | Pruebas automatizadas |

## Hoja de ruta

| Hito | Descripcion | Estado |
|---|---|---|
| 01 | Ubuntu, Distrobox y Python | Completado |
| 02 | Git, GitHub y SSH | Completado |
| 03 | Documentacion y pruebas | Completado |
| 04 | CI con GitHub Actions | Completado |
| 05 | DevSecOps y seguridad | Pendiente |
| 06 | Ramas y Pull Requests | Pendiente |
| 07 | API REST con FastAPI | Pendiente |
| 08 | Contenedores Podman | Pendiente |
| 09 | Kubernetes local | Pendiente |
| 10 | Prometheus y Grafana | Pendiente |
| 11 | GitOps con Flux CD | Pendiente |
| 12 | IA y agentes para SRE | Pendiente |
| 13 | Proyecto integrador final | Pendiente |

## Implementaciones realizadas

### Hito 01 - Entorno de desarrollo

Configuracion de Ubuntu 24.04 mediante
Distrobox en Steam Deck LCD.

- Entorno Python funcional
- Entorno virtual .venv
- Primer programa main.py
- Desarrollo remoto desde iPhone

### Hito 02 - Git y GitHub

Implementacion de control de versiones.

- Repositorio remoto GitHub
- Autenticacion SSH con clave Ed25519
- Commits y publicacion de cambios
- Sincronizacion de la rama main

### Hito 03 - Documentacion y testing

Se implemento un programa interactivo
con pruebas automatizadas.

Funciones:
- Saludar utilizando un nombre
- Solicitar entrada por consola
- Utilizar Mundo como nombre por defecto

Pruebas:
- test_saludo_nombre
- test_ingreso_nombre
- test_nombre_vacio

Resultado local: 3 pruebas correctas.

Comando:
`python3 -m unittest discover -s tests -v`

### Hito 04 - Integracion continua

Implementacion del pipeline Python CI.

Archivo:
`.github/workflows/python-ci.yml`

Caracteristicas:
- Ejecucion ante push a main
- Ejecucion en Pull Requests a main
- Runner Linux de GitHub
- Python 3.12
- Ejecucion automatica de unittest

[Ver ejecuciones CI](https://github.com/piperodriguez2024/hola-python/actions)

## Evidencias

Commits principales:

- Hito 02: 9ad1534 - Saludo interactivo
- Hito 03: da8a12f - README y gitignore
- Hito 03: 541ede1 - Pruebas automatizadas
- Hito 04: a9321f6 - Pipeline GitHub Actions

## Ejecutar el proyecto

Desde el entorno Ubuntu:

`cd ~/proyectos/hola-python`

Ejecutar:
`python3 main.py`

Ejecutar pruebas:
`python3 -m unittest discover -s tests -v`

## Proximas implementaciones

Hito 05:
Incorporar controles de seguridad, analisis
estatico y deteccion de vulnerabilidades.

Hito 12:
Implementar un agente de Inteligencia
Artificial capaz de analizar alertas,
metricas y logs para recomendar
acciones SRE supervisadas.

## Evolucion del laboratorio

Cada hito incorporara:
- Objetivo tecnico
- Arquitectura implementada
- Configuraciones y codigo
- Pruebas y resultados
- Evidencias verificables
- Commits y siguientes pasos

Proyecto educativo y de portafolio tecnico.
