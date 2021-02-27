from django.urls import path, include
from catalog.views import IndexView, EmployeeDetail, GovernanceView, ResultsView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('', include('django.contrib.auth.urls')),
    path('employee/<int:pk>', EmployeeDetail.as_view(), name='employee'),
    path('governance/', GovernanceView.as_view(), name='governance'),
    path('results/', ResultsView.as_view(), name='results'),
]