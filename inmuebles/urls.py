from django.urls import path  
from . import views 

urlpatterns = [    
    path('', views.inmueble_view, name='inmueble'),
    path('<int:id>/', views.detalle_view, name='detalle')
]