"""
Configuração da aplicação 'store'.
"""

from django.apps import AppConfig


class StoreConfig(AppConfig):
    """Configurações padrões para o app store."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "store"
