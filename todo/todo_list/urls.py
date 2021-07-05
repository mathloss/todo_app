from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('apropos/', views.apropos, name='apropos'),
path('delete/<list_id>', views.delete, name='delete'),
path('cocher/<list_id>', views.cocher, name='cocher'),
path('decocher/<list_id>', views.decocher, name='decocher'),
path('editer/<list_id>', views.editer, name='editer'),
    
]
