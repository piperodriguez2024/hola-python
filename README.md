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
| 05 | DevSecOps y seguridad | Completado |
| 06 | Ramas y Pull Requests | Completado |
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


### Hito 05 - DevSecOps y seguridad automatizada

**Objetivo:** Integrar controles de seguridad
en el ciclo de desarrollo Python.

#### Controles implementados

| Control | Herramienta | Resultado |
|---|---|---|
| Pruebas unitarias | unittest | PASS |
| Analisis estatico SAST | Bandit | PASS |
| Auditoria de paquetes | pip-audit | PASS |

#### Remediacion de vulnerabilidades

Durante la auditoria local se detectaron
12 registros de vulnerabilidad en pip 24.0,
incluidos identificadores repetidos.

Acciones realizadas:

1. Identificacion con pip-audit.
2. Actualizacion de pip 24.0 a 26.3.
3. Nueva auditoria sin hallazgos conocidos.
4. Validacion de las tres pruebas unitarias.

La actualizacion se realizo exclusivamente
dentro del entorno virtual Python.

#### Integracion continua

El pipeline ejecuta tres trabajos:

- Pruebas unitarias
- Analisis de seguridad SAST
- Auditoria de dependencias del runner

La auditoria actual del runner no sustituye
una auditoria especifica de las dependencias
de la aplicacion. Esta se incorporara cuando
el proyecto tenga dependencias declaradas.

**Resultado:** Python CI #4 exitoso
en 14 segundos.

**Commit:** 62d02cb

[Ver ejecuciones de seguridad](https://github.com/piperodriguez2024/hola-python/actions)

#### Competencias demostradas

- DevSecOps
- SAST con Bandit
- Auditoria de vulnerabilidades
- Remediacion de dependencias
- Seguridad integrada en CI
- Validacion automatizada


### Hito 06 - Git avanzado y Pull Requests

**Objetivo:** Implementar un flujo profesional
de desarrollo basado en ramas y revisiones.

#### Implementaciones

- Rama feature/hito-06-flujo-pr
- Desarrollo independiente de main
- Commit y publicacion de rama remota
- Creacion del Pull Request #1
- Revision de cambios en GitHub
- Integracion mediante merge

#### Pruebas agregadas

Archivo: tests/test_casos_borde.py

- Validacion de nombres con espacios
- Validacion de caracteres acentuados

Resultado: 5 pruebas unitarias exitosas.

#### Controles DevSecOps

Todos los controles del PR fueron aprobados:

- Pruebas unitarias
- Bandit SAST
- Auditoria de dependencias

#### Evidencia

[Pull Request #1](https://github.com/piperodriguez2024/hola-python/pull/1)

**Competencias demostradas:**
Git branching, Pull Requests, revision
de codigo, merge y CI/CD.

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
