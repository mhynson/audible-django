from django.urls import path
from . import views

urlpatterns = [
  path('', views.dashboard),
  # path('login', views.login),
  # path('logout', views.logout),
  path('register', views.register),
  # path('book/add', views.book_add),
  # path('book/remove', views.book_remove),
]