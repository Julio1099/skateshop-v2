#!/usr/bin/env bash
# exit on error
set -o errexit

# 1. Instala dependências (incluindo Gunicorn e Whitenoise)
pip install -r requirements.txt

# 2. Arruma os arquivos estáticos (CSS/Imagens do sistema)
python manage.py collectstatic --no-input

# 3. Cria as tabelas no Banco de Dados (Postgres)
python manage.py migrate

python manage.py createsuperuser --noinput || true
