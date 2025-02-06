from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

from apps.user.views import UserViewSet, GroupViewSet

def trigger_error(request):
    division_by_zero = 1 / 0


router = routers.DefaultRouter()
router.register(r'admin/users', UserViewSet)
router.register(r'admin/groups', GroupViewSet)


docs_urls = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('docs/', include(docs_urls)),
    path('sentry-debug/', trigger_error),
]