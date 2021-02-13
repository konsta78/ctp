from django.urls import path
from catalog.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
]