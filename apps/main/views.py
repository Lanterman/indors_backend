from django.utils.decorators import method_decorator
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

from . import models, serializers, permissions


@method_decorator(name="get", decorator=swagger_auto_schema(tags=["cats"]))
@method_decorator(name="post", decorator=swagger_auto_schema(tags=["cats"]))
class ListCatView(generics.ListCreateAPIView):
    """List user cats and create a cat endpoints"""

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return models.Cat.objects.filter(owner_id_id=self.request.user.id)

    def get_serializer_class(self):
        if self.request.method == "POST":
            return serializers.CreateCatSerializer
        elif self.request.method == "GET":
            return serializers.CatSerializer
    
    def perform_create(self, serializer):
        serializer.save(owner_id=self.request.user)


@method_decorator(name="get", decorator=swagger_auto_schema(tags=["cat"]))
@method_decorator(name="put", decorator=swagger_auto_schema(tags=["cat"]))
@method_decorator(name="patch", decorator=swagger_auto_schema(tags=["cat"]))
@method_decorator(name="delete", decorator=swagger_auto_schema(tags=["cat"]))
class CatView(generics.RetrieveUpdateDestroyAPIView):
    """Cat endpoint"""

    queryset = models.Cat.objects.all()
    permission_classes = [IsAuthenticated, permissions.IsOwner]
    lookup_field = "id"

    def get_serializer_class(self):
        if self.request.method in ("PUT", "PATCH", "POST"):
            return serializers.UpdateCatSerializer
        elif self.request.method == "GET":
            return serializers.CatSerializer
 