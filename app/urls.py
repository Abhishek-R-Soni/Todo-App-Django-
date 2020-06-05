from django.urls import path
from app import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'app'

urlpatterns = [
    path('index/', views.TodoListView.as_view(), name = 'index'),
    path('delete/<int:pk>/', views.TodoDeleteView.as_view(), name='delete'),
    path('add/', views.addTodo, name = 'add'),
    path('make_completed/<int:pk>/', views.make_completed, name = 'make_completed'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/',views.register, name='register'),
    path('logout/',LogoutView.as_view(), name = 'logout')
]
