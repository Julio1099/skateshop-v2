# 1. Escolhemos a imagem base (Python 3.11 "magrinho")
FROM python:3.11-slim

# 2. Configurações para o Python não travar no Docker
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Define a pasta de trabalho dentro da caixa
WORKDIR /app

# 4. Copia a lista de ingredientes e instala
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# 5. Copia todo o resto do código para dentro
COPY . /app/

# 6. Comando para rodar o servidor quando a caixa ligar
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]