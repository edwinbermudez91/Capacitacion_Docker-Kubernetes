<div align="center">

# 🐳☸️ Capacitación Práctica: Fundamentos de Docker y Kubernetes

[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](./laboratorios/lab1-docker/ejercicio-docker.md)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)](./laboratorios/lab2-kubernetes/)
[![FastAPI](https://img.shields.io/badge/FastAPI_Multi--Stage-009688?style=for-the-badge&logo=fastapi&logoColor=white)](./laboratorios/lab1-docker/translate/README.md)
[![Autor](https://img.shields.io/badge/Instructor-Edwin_Bermúdez-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/edwin-bermudez-cuervo)

**Repositorio oficial de capacitación práctica diseñado para llevarte desde la creación y optimización de imágenes con Docker hasta el despliegue de aplicaciones Stateless y Stateful en clústeres de Kubernetes.**

</div>

---

## 🗺️ Estructura del Repositorio

```text
Capacitacion_Docker-Kubernetes/
├── 🎓 presentaciones/
│   └── Capacitacion-Docker_Kubernetes.pdf   # Diapositivas oficiales de soporte teórico
└── 💻 laboratorios/
    ├── 🐳 lab1-docker/
    │   ├── ejercicio-docker.md              # Guía práctica: imágenes, puertos y Multi-stage builds
    │   └── translate/                       # Proyecto real: API FastAPI + Multi-stage + No-Root + Healthcheck
    └── ☸️ lab2-kubernetes/
        ├── ejercicio-stateless.md           # Guía práctica: Deployment + ConfigMap + Service NodePort
        ├── stateless/                       # Manifiestos YAML de la aplicación Stateless (webapp-color)
        ├── ejercicio-stateful.md            # Guía práctica: StatefulSet MySQL + Secret + Headless Service + Adminer
        └── stateful/                        # Manifiestos YAML de la arquitectura Stateful
```

---

## 📚 Ruta de Aprendizaje y Laboratorios

| Módulo | Laboratorio / Recurso | Qué aprenderás | Enlace Directo |
| :---: | :--- | :--- | :---: |
| **0️⃣ Teoría** | **Presentación Oficial (PDF)** | Conceptos clave de contenedores, arquitectura de Docker, arquitectura de Kubernetes y objetos principales. | [📄 Ver PDF](./presentaciones/Capacitacion-Docker_Kubernetes.pdf) |
| **1️⃣ Docker Básico y Optimización** | **Lab 1A: Fundamentos y Multi-Stage** | Creación de `Dockerfile`, contenedores en background (`-d`), mapeo de puertos (`-p`) y reducción de tamaño con **Multi-stage builds**. | [🐳 Ir al Lab 1A](./laboratorios/lab1-docker/ejercicio-docker.md) |
| **2️⃣ Docker en Producción** | **Lab 1B: Secure Translator (FastAPI)** | Empaquetado de una app web real con **Multi-stage build**, usuario **no-root (`appuser`)** y monitoreo automático con `HEALTHCHECK`. | [🔐 Ir al Lab 1B](./laboratorios/lab1-docker/translate/README.md) |
| **3️⃣ Kubernetes Stateless** | **Lab 2A: App Web Sin Estado** | Despliegue de réplicas con `Deployment`, inyección de variables con `ConfigMap` y exposición mediante `Service (NodePort)`. | [☸️ Ir al Lab 2A](./laboratorios/lab2-kubernetes/ejercicio-stateless.md) |
| **4️⃣ Kubernetes Stateful** | **Lab 2B: Base de Datos Con Estado** | Gestión de credenciales con `Secret`, despliegue de **MySQL** con `StatefulSet` + *Headless Service* y conexión visual desde **Adminer**. | [🗄️ Ir al Lab 2B](./laboratorios/lab2-kubernetes/ejercicio-stateful.md) |

---

## 🛠️ Requisitos Previos

Puedes realizar todos los laboratorios en tu equipo local o directamente desde el navegador:

1. **Entorno de Contenedores (Docker):**
   - **En la nube (recomendado sin instalar nada):** [iximiuz Labs](https://labs.iximiuz.com/) o [Play with Docker](https://labs.play-with-docker.com/).
   - **En tu máquina local:** [Docker Desktop](https://www.docker.com/products/docker-desktop/) o Docker Engine en Linux.
2. **Clúster de Kubernetes (para el Lab 2):**
   - `Minikube`, `kind`, Kubernetes integrado en Docker Desktop o un playground de Kubernetes en [iximiuz Labs](https://labs.iximiuz.com/).
   - Herramienta de línea de comandos `kubectl` instalada.

---

## 🏁 Cómo Empezar

1. **Clona este repositorio** en tu máquina o entorno de laboratorio:
   ```bash
   git clone https://github.com/edwinbermudez91/Capacitacion_Docker-Kubernetes.git
   cd Capacitacion_Docker-Kubernetes
   ```
2. **Revisa la teoría** abriendo [`presentaciones/Capacitacion-Docker_Kubernetes.pdf`](./presentaciones/Capacitacion-Docker_Kubernetes.pdf).
3. **Ejecuta los laboratorios paso a paso:**
   - Inicia con Docker: [`laboratorios/lab1-docker/ejercicio-docker.md`](./laboratorios/lab1-docker/ejercicio-docker.md)
   - Continúa con Kubernetes Stateless: [`laboratorios/lab2-kubernetes/ejercicio-stateless.md`](./laboratorios/lab2-kubernetes/ejercicio-stateless.md)
   - Finaliza con Kubernetes Stateful: [`laboratorios/lab2-kubernetes/ejercicio-stateful.md`](./laboratorios/lab2-kubernetes/ejercicio-stateful.md)

---

## 👨‍🏫 Autor y Comunidad

Material creado y mantenido por **Edwin Bermúdez** — *Senior DevOps & SRE | Cloud Native Instructor*.

- 🔗 **LinkedIn:** [linkedin.com/in/edwin-bermudez-cuervo](https://www.linkedin.com/in/edwin-bermudez-cuervo)
- 🐙 **GitHub:** [@edwinbermudez91](https://github.com/edwinbermudez91)
- 🚢 **¿Quieres profundizar aún más?** Explora nuestro curso de 6 semanas [**De Cero a Capitán en Kubernetes (`Fundamentos-Kubernetes`)**](https://github.com/edwinbermudez91/Fundamentos-Kubernetes).
