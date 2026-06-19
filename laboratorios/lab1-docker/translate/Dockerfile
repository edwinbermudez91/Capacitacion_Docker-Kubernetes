# ---- Etapa 1: Dependencias ----
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .

# Genera wheels precompilados para evitar herramientas de build en la imagen final
RUN pip install --no-cache-dir --upgrade pip \
    && pip wheel --no-cache-dir --no-deps --wheel-dir /wheels -r requirements.txt


# ---- Etapa 2: Imagen final ----
FROM python:3.11-slim

# Crear usuario no-root para mayor seguridad
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

WORKDIR /app

# Instalar wheels sin herramientas de compilación
COPY --from=builder /wheels /wheels
RUN pip install --no-cache-dir /wheels/* && rm -rf /wheels

# Copiar solo los archivos necesarios
COPY --chown=appuser:appgroup translate.py app.py index.html ./

USER appuser

EXPOSE 8000

# Healthcheck para que Docker monitoree el estado del contenedor
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/')" || exit 1

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
