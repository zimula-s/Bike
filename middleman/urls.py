"""
URL configuration for middleman project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from manager.views import index_view,boda_view,rider_view,customer_view,trip_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name = 'index_page'),
    path('boda_view/',boda_view, name = 'boda_page'),
    path('rider_view/',rider_view, name = 'rider_page'),
    path('customer_view/',customer_view, name = 'customer_page'),
    path('trip_view/',trip_view, name = 'trip_page')
]
