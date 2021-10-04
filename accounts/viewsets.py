from rest_framework import viewsets
from accounts import serializers
from accounts import models


class ArchiveViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ArquiveSerializer
    queryset = models.Archive.objects.all()
