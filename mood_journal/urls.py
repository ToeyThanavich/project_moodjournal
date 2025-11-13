# mood_journal/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.generic import TemplateView

# API Documentation Schema
schema_view = get_schema_view(
    openapi.Info(
        title="Mood Journal API",
        default_version='v1',
        description="API สำหรับระบบ Mood Journal ที่ใช้ JWT Authentication และ AIforthai Sentiment Analysis",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@moodjournal.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # API Documentation
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/docs/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/docs/json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    
    # API endpoints
    path('api/accounts/', include('accounts.urls')),
    path('api/journal/', include('journal.urls')),
    
    # Frontend views
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
    path('register/', TemplateView.as_view(template_name='register.html'), name='register'),
    path('dashboard/', TemplateView.as_view(template_name='dashboard.html'), name='dashboard'),
    path('journal/', TemplateView.as_view(template_name='journal_entry.html'), name='journal_entry'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)