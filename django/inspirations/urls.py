from django.urls import path
from . import views

app_name = 'inspirations'

urlpatterns = [
    path('', views.InspirationListView.as_view(), name='inspiration-list'),
    path('<int:pk>/', views.InspirationDetailView.as_view(), name='inspiration-detail'),
]
