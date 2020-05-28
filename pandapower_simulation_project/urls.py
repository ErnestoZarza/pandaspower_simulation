"""pandapower_simulation_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from pandapower_simulation_api.views import ActivePowerView, ReactivePowerView, SimulationView



urlpatterns = [
    path('admin/', admin.site.urls),
    url('^pandapower_api/simulation/create/', SimulationView.as_view(),name='create-simulation'),
    url('^pandapower_api/simulation/active/', ActivePowerView.as_view(), name='active-power-detail'),
    url('^pandapower_api/simulation/reactive/', ReactivePowerView.as_view(), name='reactive-power-detail'),

]
