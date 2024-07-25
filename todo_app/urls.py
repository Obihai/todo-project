from django.urls import path
from .views import TodoListView, TodoToggleComplete

urlpatterns = [
    path('', TodoListView.as_view(), name='todo_list'),
    path('toggle/<int:pk>/', TodoToggleComplete.as_view(), name='toggle_complete'),
]