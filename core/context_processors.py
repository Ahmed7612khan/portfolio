# core/context_processors.py
from .models import SiteSettings

def site_settings(request):
    settings = SiteSettings.objects.first()
    return {
        'site_settings': settings,
        'current_theme': request.session.get('theme', 'light'),
    }