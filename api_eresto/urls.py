"""
URL configuration for api_eresto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

from django.urls import re_path
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.conf.urls.static import static
from users.api.router import router_user
from categories.api.router import router_category
from products.api.router import router_product
from tables.api.router import router_table
from orders.api.router import router_orders
from payments.api.router import router_payments
from django.urls import path

def trigger_error(request):
    division_by_zero = 1 / 0
schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API eRestó",
        default_version='v1',
        description="Documentacion de API eResto",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="jmunoz@lawentech.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('sentry-debug/', trigger_error),
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
    path('api/', include('users.api.router')),
    path('api/', include(router_user.urls)),
    path('api/', include(router_category.urls)),
    path('api/', include(router_product.urls)),
    path('api/', include(router_table.urls)),
    path('api/', include(router_orders.urls)),
    path('api/', include(router_payments.urls))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
