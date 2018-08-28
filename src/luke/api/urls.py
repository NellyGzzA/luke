# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include, url

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework.permissions import AllowAny

urlpatterns = [
    url(
        r'^v1/', include('luke.api.v1.urls', namespace='v1')
    ),
]

if not settings.PRODUCTION:
    schema_view = get_schema_view(
        openapi.Info(
            title="API DOC",
            default_version='v1',
            description="API for demo",
        ),
        validators=['flex'],
        public=True,
        permission_classes=(AllowAny,),
    )
    urlpatterns += [
        url(
            r'^docs',
            schema_view.with_ui('redoc', cache_timeout=None),
            name='schema-redoc'
        ),
    ]
