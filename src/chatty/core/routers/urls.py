from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view
from rest_framework.permissions import AllowAny
from django.conf.urls import (handler400, handler403, handler404, handler500)

handler400 = 'api.user.routers.views.handler'
handler403 = 'api.user.routers.views.handler'
handler404 = 'api.user.routers.views.handler'
handler500 = 'api.user.routers.views.handler'


schema_view = swagger_get_schema_view(
    openapi.Info(title="RemoFirst API", default_version="v1", description="RemoFirst API documentation"),
    public=True,
    permission_classes=[AllowAny],
)


urlpatterns = [
    path("", lambda req: redirect("schema-swagger-ui")),
    path("admin/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path(
        "api/v1/",
        include(
            [
                path("users/", include("api.user.routers.urls")),
                path("chats/", include("api.chat.routers.urls")),
                path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
            ]
        ),
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
