from drf_yasg.views import get_schema_view
from drf_yasg import openapi


from django.contrib import admin
from django.urls import include, path


schema_view = get_schema_view(
   openapi.Info(
      title="Broker",
      default_version='v1',
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/payments/', include('payments.urls', namespace='payments')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]