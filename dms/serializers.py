from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from dms.models import Message


"""
Serialize Messages model into JSON-data
"""


class MessageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    receiver_name = serializers.ReadOnlyField(source='receiver.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        """Timestamp of message"""
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        """Timestamp when message edited"""
        return naturaltime(obj.updated_at)

    class Meta:
        model = Message
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'receiver', 'receiver_name', 'text', 'created_at',
            'updated_at',
        ]
