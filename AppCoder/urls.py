from django.urls import path
from AppCoder import views

urlpatterns = [
    path('inicio/', views.inicio, name="Inicio"),
    path('profesores/', views.profesores, name="Profesores"),
    path('estudiantes/', views.estudiantes, name="Estudiantes"),
    path('cursos/', views.cursos, name="Cursos"),
    path('entregables/', views.entregables, name="Entregables"),
    path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
    path('apicursoForm', views.apiCursoFormulario, name="apiCursoForm"), 
]