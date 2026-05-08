# 🚀 Fundamentos Docker, Kubernetes y AKS

¡Bienvenido al repositorio oficial del curso! Aquí encontrarás todo el material necesario para la capacitación, diseñado para llevarte desde los conceptos básicos de la creación de contenedores hasta el despliegue de aplicaciones en cluster de kubernetes.

## 📁 Contenido del Repositorio

- 🎓 **`presentaciones/`**: Contenido de las diapositivas en formato Markdown, listas para acompañar la teoría.
- 💻 **`laboratorios/`**: El núcleo práctico del curso. Contiene guías paso a paso y manifiestos listos para aplicar:
  - 🐳 `lab1-docker/`: Creación de imágenes, contenedores interactivos, mapeo de puertos y optimización con *Multi-stage builds*.
  - ☸️ `lab2-kubernetes/`: Prácticas esenciales divididas en dos enfoques:
    - **Stateless:** Despliegue de una app web dinámica inyectando configuración vía `ConfigMaps`.
    - **Stateful:** Implementación de una base de datos con `StatefulSets`, gestión de credenciales con `Secrets` y conexión mediante un frontend web (`Adminer`).
- 📊 **`diagramas/`**: Archivos editables en draw.io para visualizar la arquitectura de nuestros clústeres.

## 🛠️ Requisitos Previos

Para aprovechar al máximo este material, necesitarás:
- **Contenedores:** Docker instalado en tu máquina local, o acceso a plataformas web como labs.iximiuz.com o Play with Docker.
- **Kubernetes Local:** `Minikube` o `kind` instalados y configurados para ejecutar el Lab 2.

## 🏁 Cómo Empezar

1. **Clona** este repositorio en tu equipo local.
2. **Explora** la carpeta `presentaciones/` para repasar o seguir la teoría.
3. **Practica** ingresando a cada carpeta dentro de los laboratorios (por ejemplo, `cd lab1-docker/`).
4. **Sigue las guías** (los archivos `.md`) ejecutando los comandos paso a paso.

¡Mucho éxito en tu aprendizaje! Si experimentas o rompes algo en tu entorno local... ¡felicidades, así es como más se aprende! 🎉