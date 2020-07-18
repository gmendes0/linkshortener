from rest_framework import serializers


class LinkSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    original = serializers.CharField(max_length=255)
    hashed = serializers.CharField(max_length=20, read_only=True)
    clicks = serializers.IntegerField(read_only=True)
