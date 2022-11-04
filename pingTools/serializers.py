from rest_framework import serializers
from .models import DataTerminals

class DataTerminalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    switch = models.CharField(required=True, allow_blank=True, max_length=50)
    terminal_1 = models.IntegerField(required=True, allow_blank=True)
    terminal_2 = models.IntegerField(required=True, allow_blank=True)
    terminal_3 = models.IntegerField(required=True, allow_blank=True)
    terminal_4 = models.IntegerField(required=True, allow_blank=True)
    terminal_5 = models.IntegerField(required=True, allow_blank=True)
    switch_status = models.IntegerField(required=True, allow_blank=True)
    timestamp = models.IntegerField(required=True, allow_blank=True)
    date = models.DateTimeField(required=True, allow_blank=True)

    def create(self, validated_data):
        """
        Create and return a new `data terminals` instance, given the validated data.
        """
        return DataTerminals.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `data terminals` instance, given the validated data.
        """
        instance.switch = validated_data.get('switch', instance.switch)
        instance.terminal_1 = validated_data.get('terminal_1', instance.terminal_1)
        instance.terminal_2 = validated_data.get('terminal_2', instance.terminal_2)
        instance.terminal_3 = validated_data.get('terminal_3', instance.terminal_3)
        instance.terminal_4 = validated_data.get('terminal_4', instance.terminal_4)
        instance.terminal_5 = validated_data.get('terminal_5', instance.terminal_5)
        instance.switch_status = validated_data.get('switch_status', instance.switch_status)
        instance.timestamp = validated_data.get('timestamp', instance.timestamp)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance