from django.apps import AppConfig


class SecureConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'secure'

def ready(self):
        import secure.signals  # Ensure this line is included