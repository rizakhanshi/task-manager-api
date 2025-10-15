from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'priority', 'status', 'owner', 'completed_at', 'created_at', 'updated_at']
        read_only_fields = ['id', 'owner', 'completed_at', 'created_at', 'updated_at']

    def validate(self, attrs):
        # Prevent editing completed tasks
        instance = getattr(self, 'instance', None)
        if instance and instance.status == Task.STATUS_COMPLETED:
            raise serializers.ValidationError('Cannot edit a completed task. Mark it incomplete first.')
        return attrs
