from django.urls import path, include
from catalog.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('', include('django.contrib.auth.urls')),
]