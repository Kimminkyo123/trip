from django.contrib import admin
from django.urls import path, include
import firstapp.views
from django.conf import settings
from django.conf.urls.static import static
from .views import UserCreateView
from django.conf import settings
import freeboard.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', firstapp.views.main, name="main"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', UserCreateView.as_view(), name='register'),
    path('freeboard/', include('freeboard.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
