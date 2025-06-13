from django.apps import AppConfig


class UserfollowConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'userfollow'
    
    def ready(self):
        import userfollow.signals
        
# This ensures that the signals are imported when the app is ready.