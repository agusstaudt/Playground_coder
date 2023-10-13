# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso, ApiCurso
from AppCoder.forms import CursoFormulario, BuscaCursoForm

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def cursos(request):
    return HttpResponse("Vista cursos")

def profesores(request):
    return HttpResponse("Vista profesores")

def estudiantes(request):
    return HttpResponse("Vista estudiantes")

def entregables(request):
    return HttpResponse("Vista entregables")

def cursoFormulario(request):
    if request.method == "POST":
        miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()
            return render(request, "AppCoder/inicio.html") 
    else:
        miFormulario = CursoFormulario()
    return render(request, "AppCoder/cursoFormulario.html", {"miFormulario": miFormulario})

def apiCursoFormulario(request):

    if request.method == 'POST':
        curso = ApiCurso(request.post['nombre'],(request.post['comision']))
        curso.save()
        return render(request, "AppCoder/inicio.html")
    return render(request,"AppCoder/apiCursoFormulario.html")

def buscar(request):
    if request.method == "POST":
        miFormulario = BuscaCursoForm(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            cursos = Curso.objects.filter(nombre__icontains=informacion['curso'])

            return render(request, "AppCoder/lista.html", {'cursos':cursos}) 
    else:
        miFormulario = BuscaCursoForm()
    return render(request, "AppCoder/cursoFormulario.html", {"miFormulario": miFormulario})

def mostrar(request):
    pass