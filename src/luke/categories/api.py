# -*- coding: utf-8 -*-
from luke.api.v1.routers import router

from luke.categories import serializers
from luke.categories.models import Category
from luke.core.api.mixins import CreateModelMixin, ListModelMixin
from luke.core.api.viewsets import GenericViewSet


class CategoryViewSet(
    CreateModelMixin,
    ListModelMixin,
    GenericViewSet
):
    serializer_class = serializers.CategorySerializer
    create_serializer_class = serializers.CategoryCreateSerializer
    retrieve_serializer_class = serializers.CategorySerializer
    list_serializer_class = serializers.CategorySerializer

    def get_queryset(self, *args, **kwargs):
        is_active = self.request.query_params.get('active', False)
        is_active = True if is_active == 'true' else False
        return Category.objects.filter(active=is_active)


router.register(
    r"categories",
    CategoryViewSet,
    base_name="categories",
)
