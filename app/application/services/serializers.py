from rest_framework import response, serializers

from app.models import Email


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        exclude = ['created_document_timestamp']

    def create(self, data):
        return Email.objects.create(**data)


class StatisticsSerializer(serializers.Serializer):
    destination = serializers.CharField(max_length=150)
    total = serializers.IntegerField()
