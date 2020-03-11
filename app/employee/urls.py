from django.urls import path

from employee import views


app_name = 'employee'

urlpatterns = [
    path('create/', views.CreateEmployeeView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
]
