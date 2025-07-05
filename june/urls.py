"""
URL configuration for june project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.views.generic import TemplateView
from managementApp.views import dashboard, allProducts, viewProduct, addProduct, stockLogView
from django.conf.urls.static import static  
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="index.html"), name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('products/', allProducts, name='products'),
    path('view-product/<int:id>/', viewProduct, name='view-product'),
    path('add-product/', addProduct, name='add-product'),
    path('log-stock/<int:product_id>/', stockLogView, name='log-stock'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

