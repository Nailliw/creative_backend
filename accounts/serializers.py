from rest_framework import serializers
from accounts import models


class ArquiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Archive
        fields = "__all__"
