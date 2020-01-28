from __future__ import (absolute_import, division, print_function, unicode_literals)

from rest_framework import viewsets, permissions

from .models import data_service, deployment_status, domain, flow, product, task
from .serializers import data_serviceSerializer, deployment_statusSerializer, domainSerializer, flowSerializer, productSerializer, taskSerializer

class data_serviceViewSet(viewsets.ModelViewSet):
    queryset = data_service.objects.all()
    serializer_class = data_serviceSerializer
    # permission_classes = [permissions.IsAuthenticated]

class deployment_statusViewSet(viewsets.ModelViewSet):
    queryset = deployment_status.objects.all()
    serializer_class = deployment_statusSerializer
    # permission_classes = [permissions.IsAuthenticated]

class domainViewSet(viewsets.ModelViewSet):
    queryset = domain.objects.all()
    serializer_class = domainSerializer
    # permission_classes = [permissions.IsAuthenticated]

class flowViewSet(viewsets.ModelViewSet):
    queryset = flow.objects.all()
    serializer_class = flowSerializer
    # permission_classes = [permissions.IsAuthenticated]

class productViewSet(viewsets.ModelViewSet):
    queryset = product.objects.all()
    serializer_class = productSerializer
    # permission_classes = [permissions.IsAuthenticated]

class taskViewSet(viewsets.ModelViewSet):
    queryset = task.objects.all()
    serializer_class = taskSerializer
    # permission_classes = [permissions.IsAuthenticated]

