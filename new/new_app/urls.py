"""
Do not modify this file. It is generated from the Swagger specification.

Routing module.
"""
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
import new_app.views as views
from rest_framework import routers
from .api import data_serviceViewSet, deployment_statusViewSet, domainViewSet, flowViewSet, flow_versionViewSet, productViewSet, taskViewSet
router = routers.SimpleRouter()
router.register(r'default_crud/data_service', data_serviceViewSet)
router.register(r'default_crud/deployment_status', deployment_statusViewSet)
router.register(r'default_crud/domain', domainViewSet)
router.register(r'default_crud/flow', flowViewSet)
router.register(r'default_crud/flow_version', flow_versionViewSet)
router.register(r'default_crud/product', productViewSet)
router.register(r'default_crud/task', taskViewSet)

urlpatterns = [
    url(r"^tasks/(?P<id>.+)/version$", views.TasksIdVersion.as_view()),
    url(r"^tasks/(?P<id>.+)/publish$", views.TasksIdPublish.as_view()),
    url(r"^tasks/(?P<id>.+)$", views.TasksId.as_view()),
    url(r"^tasks$", views.Tasks.as_view()),
    url(r"^products$", views.Products.as_view()),
    url(r"^flows/(?P<id>.+)/versions$", views.FlowsIdVersions.as_view()),
    url(r"^flows/(?P<id>.+)/status$", views.FlowsIdStatus.as_view()),
    url(r"^flows/(?P<id>.+)/load/(?P<version>.+)$", views.FlowsIdLoadVersion.as_view()),
    url(r"^flows/(?P<id>.+)/deploy/(?P<env>.+)$", views.FlowsIdDeployEnv.as_view()),
    url(r"^flows/(?P<id>.+)$", views.FlowsId.as_view()),
    url(r"^flows$", views.Flows.as_view()),
    url(r"^domains/(?P<id>.+)/data-service-init$", views.DomainsIdDataServiceInit.as_view()),
    url(r"^domains/(?P<id>.+)/data-service$", views.DomainsIdDataService.as_view()),
    url(r"^domain$", views.Domains.as_view()),
]

if settings.DEBUG:
    urlpatterns.extend([
        url(r"^the_specification/$", views.__SWAGGER_SPEC__.as_view()),
        url(r"^ui/(?P<path>.*)$", serve, {"document_root": "ui",
                                          "show_indexes": True})
    ])

urlpatterns += router.urls
