from django.contrib import admin
from django.urls import path

from todos.views import TodoCreateView, TodoListView, TodoUpdateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TodoListView.as_view(), name="todo_list"),
    path("create/", TodoCreateView.as_view(), name="todo_create"),
    path("update/<int:pk>/", TodoUpdateView.as_view(), name="todo_update"),
]
