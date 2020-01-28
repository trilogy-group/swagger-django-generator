
from __future__ import (absolute_import, division, print_function, unicode_literals)

from django.contrib import admin
from django import forms
from .models import data_service, deployment_status, domain, flow, product, task
admin.site.register(data_service)
admin.site.register(deployment_status)
admin.site.register(domain)
admin.site.register(flow)
admin.site.register(product)
admin.site.register(task)
