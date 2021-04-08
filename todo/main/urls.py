from django.urls import path
from .views import Task, TaskDetail, TaskCreate, TaskUpdate, TaskDelete

urlpatterns = [
    path('', Task.as_view(), name = 'tasklist'),
    path('task/<int:pk>/', TaskDetail.as_view(), name = 'task'),
    path('task-create/', TaskCreate.as_view(), name = 'task_create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name = 'task_update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name = 'task_delete')
]
