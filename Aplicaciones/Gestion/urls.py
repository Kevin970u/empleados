from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_categorias),
    path('categorias/crear/', views.crear_categoria, name='crear_categoria'),
    path('categorias/editar/<int:pk>/', views.editar_categoria, name='editar_categoria'),
    path('categorias/eliminar/<int:pk>/', views.eliminar_categoria, name='eliminar_categoria'),
    path('listar_empresas/', views.listar_empresas, name='listar_empresas'),
    path('crear_empresa/', views.crear_empresa, name='crear_empresa'),
    path('editar_empresa/<int:pk>/', views.editar_empresa, name='editar_empresa'),
    path('eliminar_empresa/<int:pk>/', views.eliminar_empresa, name='eliminar_empresa'),
    path('listar_costos/', views.listar_costos, name='listar_costos'),
    path('crear_costo/', views.crear_costo, name='crear_costo'),
    path('editar_costo/<int:pk>/', views.editar_costo, name='editar_costo'),
    path('eliminar_costo/<int:pk>/', views.eliminar_costo, name='eliminar_costo')
]
