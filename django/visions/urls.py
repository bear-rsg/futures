from django.urls import path
from . import views

app_name = 'visions'

urlpatterns = [

    # Vision
    path('', views.VisionListView.as_view(), name='vision-list'),
    path('<int:pk>/', views.VisionDetailView.as_view(), name='vision-detail'),
    path('create/', views.VisionCreateView.as_view(), name='vision-create'),
    path('create/success/', views.VisionCreateSuccessTemplateView.as_view(), name='vision-create-success'),

    # Response
    path('response/', views.ResponseCreateView.as_view(), name='response-create'),
    path('response/success/', views.ResponseCreateSuccessTemplateView.as_view(), name='response-create-success'),

]
