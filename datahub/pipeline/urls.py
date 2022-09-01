## from django.urls import path, include
## from django.views.generic import RedirectView
## from material.frontend import urls as frontend_urls
## 
## from . import views
## 
## urlpatterns = [
##     #path('', views.index, name='index'),
##     path(r'', RedirectView.as_view(url='/pipeline/workflow/', permanent=False)),
##     path(r'', include(frontend_urls))
## ]

from viewflow.flow.viewset import FlowViewSet
from .flows import HelloWorldFlow


urlpatterns = FlowViewSet(HelloWorldFlow).urls