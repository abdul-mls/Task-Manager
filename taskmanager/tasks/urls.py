from django.urls import path
from .views import *

from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page="login"), name="logout"),
    path('register/', RegisterView.as_view(), name="register"),

    path('', TaskList.as_view(), name="task_list"),
    path('task/<int:pk>/', TaskDetail.as_view(), name="task_detail"),
    path('task/create/', TaskCreate.as_view(), name="task_create"),
    path('task/<int:pk>/update/', TaskUpdate.as_view(), name="task_update"),
    path('task/<int:pk>/delete/', TaskDelete.as_view(), name="task_delete"),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name ='password_reset_complete'),

]
