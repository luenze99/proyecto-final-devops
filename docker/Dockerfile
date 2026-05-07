#Builder
FROM python:3.9-slim AS builder
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends gcc python3-dev
#Crear un entorno virtual
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Imagen Final
FROM python:3.9-slim
WORKDIR /app
COPY --from=builder /opt/venv /opt/venv
COPY app.py .

#Activar el entorno virtual en la imagen final
ENV PATH="/opt/venv/bin:$PATH"

EXPOSE 5000
CMD ["python3", "app.py"]