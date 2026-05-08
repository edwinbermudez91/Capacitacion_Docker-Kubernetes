# Laboratorio 1 – Fundamentos de Docker

**Objetivo:** Familiarizarse con la creación y ejecución de contenedores.

Puedes usar:
- labs.iximiuz.com (recomendado)
- Play with Docker (play-with-docker.com)
- Docker Desktop en tu máquina local

## Pasos
### 1. Verifica la instalación

```bash
docker --version
docker run hello-world
```

### 2. Construye una imagen simple

Crear un Dockerfile

```bash
cat <<EOF > Dockerfile
FROM alpine:3.18
RUN apk add --no-cache bash
CMD ["echo", "Hola desde mi contenedor"]
EOF
```

Construir la imagen

```bash
docker build -t app_hola:1.0 .
```

### 3. Ejecuta el contenedor

```bash
docker run --rm app_hola:1.0 
```

### 4. Contenedor interactivo y en segundo plano

```bash
docker run -dit --name test alpine ash
docker exec -it test sh
# Dentro: crea un archivo
echo "datos" > /tmp/ejemplo.txt
exit
docker stop test
docker rm test
```

### 5. Mapeo de puertos (ejemplo con nginx)

```bash
docker run -d -p 8080:80 --name web nginx:alpine
curl http://localhost:8080
docker stop web && docker rm web
```

### 6. Limpieza

```bash
docker rmi app_hola:1.0 nginx:alpine alpine:latest
docker rmi hello-world:latest --force
```


### 7. Multi-stage

En esta sección compararemos el tamaño de una imagen tradicional vs una imagen utilizando **Multi-stage builds** con Python.

Primero, crearemos los archivos de nuestra aplicación de prueba:

```bash
cat <<EOF > app.py
import requests
print("¡Hola Equipo! Aplicación Python ejecutándose correctamente.")
EOF

cat <<EOF > requirements.txt
requests==2.31.0
EOF
```

#### **Opción A: Dockerfile Tradicional (Sin Multi-stage)**

Crearemos un archivo llamado `Dockerfile.normal`:

```bash
cat <<EOF > Dockerfile.normal
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
CMD ["python", "app.py"]
EOF
```

Construimos la imagen tradicional:

```bash
docker build -t python_app:normal -f Dockerfile.normal .
```

#### **Opción B: Dockerfile Multi-stage**

Ahora crearemos un `Dockerfile.multi` que utiliza una imagen inicial para compilar las dependencias (ruedas/wheels) y luego copia únicamente lo necesario a una imagen final mucho más ligera (`slim`).

```bash
cat <<EOF > Dockerfile.multi
# Etapa 1: Constructor (Builder)
FROM python:3.9 AS builder
WORKDIR /app
COPY requirements.txt .
# Generamos binarios precompilados (wheels) para no instalar herramientas de compilación en la imagen final
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

# Etapa 2: Imagen Final Ligera
FROM python:3.9-slim
WORKDIR /app
COPY --from=builder /app/wheels /wheels
COPY requirements.txt .
# Instalamos desde los wheels creados en la etapa anterior sin usar caché
RUN pip install --no-cache /wheels/*
COPY app.py .
CMD ["python", "app.py"]
EOF
```

Construimos la imagen multi-stage:

```bash
docker build -t python_app:multi -f Dockerfile.multi .
```

#### Comparación de Rendimiento y Tamaño

Ejecuta el siguiente comando para ver la diferencia de tamaño entre ambas imágenes:

```bash
docker images | grep python_app
```

### 8. Limpieza

```bash
docker rmi python_app:multi python_app:normal
```