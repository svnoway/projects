from django.urls import path
from .views import Task, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, Login, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', Login.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(next_page = 'tasklist'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', Task.as_view(), name = 'tasklist'),
    path('task/<int:pk>/', TaskDetail.as_view(), name = 'task'),
    path('task-create/', TaskCreate.as_view(), name = 'task_create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name = 'task_update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name = 'task_delete')
]
