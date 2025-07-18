"""djangoproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include # Make sure include is imported
from django.views.generic import TemplateView # Import TemplateView

urlpatterns = [

    path('admin/', admin.site.urls),
    
    # Add this line to include your app's API URLs
    path('djangoapp/', include('djangoapp.urls')),
    # Add this line to serve the React app for the login page
    path('login', TemplateView.as_view(template_name="index.html")),
    # Add this line to serve the React app for the root URL
    path('', TemplateView.as_view(template_name="index.html")),
    # path('', include('djangoapp.urls')),
    # <<< ADD THIS LINE >>>
    path('register/', TemplateView.as_view(template_name="index.html")),
    path('dealers/', TemplateView.as_view(template_name="index.html")),
    path('dealer/<int:dealer_id>', TemplateView.as_view(template_name="index.html")),
    path('postreview/<int:dealer_id>', TemplateView.as_view(template_name="index.html")),

]