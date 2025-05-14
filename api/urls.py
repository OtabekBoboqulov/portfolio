from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile),
    path('skills/', views.skills),
    path('projects/', views.projects),
    path('projects/<int:pk>/', views.project_detail),
    path('experiences/', views.experiences),
    path('education/', views.education),
    path('contact/', views.contact),
    path('data/', views.all_data),
]
