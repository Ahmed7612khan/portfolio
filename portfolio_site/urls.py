# portfolio_site/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('project/<slug:slug>/', views.project_detail, name='project_detail'),
    path('blog/', include('blog.urls')),
    path('toggle-theme/', views.toggle_theme, name='toggle_theme'),
    path('contact/submit/', views.contact_submit, name='contact_submit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)