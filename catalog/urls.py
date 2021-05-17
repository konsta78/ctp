from django.urls import path, include
from catalog.views import IndexView, EmployeeDetail, GovernanceView, \
    ResultsView, DepartmentsView, DepartmentDetail, LoadDataBaseView, \
    DeleteDataBaseView, AddressesView, UsersListView, UsersDeleteView, \
    SaveDataBaseView
from django.contrib.auth import views

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('home/', IndexView.as_view(), name='home'),
    # path('', include('django.contrib.auth.urls')),
    path('employee/<int:pk>', EmployeeDetail.as_view(), name='employee'),
    path('governance/', GovernanceView.as_view(), name='governance'),
    path('departments/', DepartmentsView.as_view(), name='department'),
    path('departments/<int:pk>', DepartmentDetail.as_view(), name='department-detail'),
    path('addresses/', AddressesView.as_view(), name='addresses'),
    path('results/', ResultsView.as_view(), name='results'),
    path('upload/', LoadDataBaseView.as_view(), name='upload_db'),
    path('save/', SaveDataBaseView.as_view(), name='save_db'),
    path('delete/', DeleteDataBaseView.as_view(), name='delete_db'),
    path('users/create', UsersListView.as_view(), name='crt_emp_users'),
    path('users/delete', UsersDeleteView.as_view(), name='del_emp_users'),
]