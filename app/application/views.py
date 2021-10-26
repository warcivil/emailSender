from datetime import datetime, timedelta

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from django.db.models import Count

from app.application.services.serializers import EmailSerializer
from app.models import Email

from app.application.services.serializers import StatisticsSerializer


class EmailView(APIView):
    def get(self, request):
        queryset = Email.objects.all()
        serializer = EmailSerializer(queryset, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201, data=serializer.data)
        return Response(status=400, data=serializer.errors)


class EmailInfoView(APIView):
    def get(self, request, pk):
        email_info = get_object_or_404(Email, pk=pk)
        if email_info:
            serializer = EmailSerializer(email_info)
            return Response(serializer.data)
        return Response(status=404, data={'status': 'not found'})


class StatisticsView(APIView):
    def get(self, request):
        date_from = datetime.now() - timedelta(days=1)
        total = Email.objects.filter(created_document_timestamp__gte=date_from).count()
        emails_top = Email.objects.filter(
            created_document_timestamp__gte=date_from).values(
            'destination').annotate(
            total=Count('destination'))[:10]

        serializer = StatisticsSerializer(emails_top, many=True)
        response = sorted(serializer.data, key=lambda x: x['total'], reverse=True)
        return Response(status=200, data={'total': total, 'ranked': response})
