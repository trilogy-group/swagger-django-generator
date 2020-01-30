from __future__ import (absolute_import, division, print_function, unicode_literals)

from rest_framework import viewsets, mixins, permissions

from .models import data_service, deployment_status, domain, flow, flow_version, product, task
from .serializers import data_serviceSerializer, deployment_statusSerializer, domainSerializer, flowSerializer, flow_versionSerializer, productSerializer, taskSerializer

class data_serviceViewSet(mixins.CreateModelMixin, 
                   mixins.RetrieveModelMixin, 
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = data_service.objects.all()
    serializer_class = data_serviceSerializer
    # permission_classes = [permissions.IsAuthenticated]

class deployment_statusViewSet(mixins.CreateModelMixin, 
                   mixins.RetrieveModelMixin, 
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = deployment_status.objects.all()
    serializer_class = deployment_statusSerializer
    # permission_classes = [permissions.IsAuthenticated]

class domainViewSet(mixins.CreateModelMixin, 
                   mixins.RetrieveModelMixin, 
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = domain.objects.all()
    serializer_class = domainSerializer
    # permission_classes = [permissions.IsAuthenticated]

class flowViewSet(mixins.CreateModelMixin, 
                   mixins.RetrieveModelMixin, 
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = flow.objects.all()
    serializer_class = flowSerializer
    # permission_classes = [permissions.IsAuthenticated]

class flow_versionViewSet(mixins.CreateModelMixin, 
                   mixins.RetrieveModelMixin, 
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = flow_version.objects.all()
    serializer_class = flow_versionSerializer
    # permission_classes = [permissions.IsAuthenticated]

class productViewSet(mixins.CreateModelMixin, 
                   mixins.RetrieveModelMixin, 
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = product.objects.all()
    serializer_class = productSerializer
    # permission_classes = [permissions.IsAuthenticated]

class taskViewSet(mixins.CreateModelMixin, 
                   mixins.RetrieveModelMixin, 
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = task.objects.all()
    serializer_class = taskSerializer
    # permission_classes = [permissions.IsAuthenticated]

