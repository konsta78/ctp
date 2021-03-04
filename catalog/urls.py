from django.urls import path, include
from catalog.views import IndexView, EmployeeDetail, GovernanceView, \
    ResultsView, DepartmentsView, DepartmentDetail, LoadDataBaseView, DeleteDataBaseView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('', include('django.contrib.auth.urls')),
    path('employee/<int:pk>', EmployeeDetail.as_view(), name='employee'),
    path('governance/', GovernanceView.as_view(), name='governance'),
    path('departments/', DepartmentsView.as_view(), name='department'),
    path('departments/<int:pk>', DepartmentDetail.as_view(), name='department-detail'),
    path('results/', ResultsView.as_view(), name='results'),
    path('upload/', LoadDataBaseView.as_view(), name='upload_db'),
    path('delete/', DeleteDataBaseView.as_view(), name='delete_db'),
]