
from django.urls import path,include
from . import views
from rest_framework import routers

#router = routers.DefaultRouter()
#router.register('',views.BorrowView)
urlpatterns = [
    path('borrows/', views.BorrowView.as_view()),
    path('borrows/<int:pk>',views.BorrowView.as_view()),
    path('borrows/delete/<int:pk>',views.BorrowView.delete_by_field),

]