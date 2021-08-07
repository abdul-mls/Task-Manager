from django.urls import path
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page="login"), name="logout"),
    path('register/', RegisterView.as_view(), name="register"),
    path('', TaskList.as_view(), name="task_list"),
    path('task/<int:pk>/', TaskDetail.as_view(), name="task_detail"),
    path('task/create/', TaskCreate.as_view(), name="task_create"),
    path('task/<int:pk>/update/', TaskUpdate.as_view(), name="task_update"),
    path('task/<int:pk>/delete/', TaskDelete.as_view(), name="task_delete"),
]
