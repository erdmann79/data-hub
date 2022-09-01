"""datahub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#from django.contrib import admin
#from django.urls import path, include
#from material.frontend import urls as frontend_urls
#
##from django.urls import include
##from .pipeline import views
#
#urlpatterns = [
#    #path('/', views.home, name='home'),
#    #path('pipeline/', include('pipeline.urls')),
#    path("admin/", admin.site.urls),
#    path('', include(frontend_urls))
#]
#
#
#urlpatterns = [
#    path('accounts/login/', auth.LoginView.as_view(), name='login'),
#    path('accounts/logout/', auth.LogoutView.as_view(), name='logout'),
#    path('', include('demo.website')),
#    path('', include(frontend_urls)),
#]




from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth
from django.views import generic

from material import frontend
from material.frontend.apps import ModuleMixin
from material.frontend.registry import modules


class Pipeline(ModuleMixin):
    """
    Home page module
    """
    order = 1
    label = 'Introduction'
    icon = '<i class="material-icons">account_balance</i>'

    @property
    def urls(self):
        index_view = generic.TemplateView.as_view(template_name='datahub/index.html')

        return frontend.ModuleURLResolver(
            '^', [path('', index_view, name="index")],
            module=self, app_name='datahub', namespace='datahub')

    def index_url(self):
        return '/'

    def installed(self):
        return True


modules.register(Pipeline())

from material.frontend import urls as frontend_urls

urlpatterns = [
    path('accounts/login/', auth.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth.LogoutView.as_view(), name='logout'),
    path("admin/", admin.site.urls),
    path('', include('datahub.website')),
    path('', include(frontend_urls)),
]