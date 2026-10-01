from django.shortcuts import render
from .models import Categoria

def crear(request):
    if request.method == "POST":
        categoria = Categoria(
            nombre=request.POST["nombre"],
            descripcion=request.POST["descripcion"]
        )
        categoria.save()
    return render(request, "categorias/formulario.html")

def listar(request):
    categorias = Categoria.objects.all()
    return render(request, "categorias/lista.html", {"categorias": categorias})

def editar(request, id):
    categoria = Categoria.objects.get(id=id)
    if request.method == "POST":
        categoria.nombre = request.POST["nombre"]
        categoria.descripcion = request.POST["descripcion"]
        categoria.save()
        return render(request, "categorias/lista.html", {"categoria": categoria})
    return render(request, "categorias/formulario.html", {"categoria": categoria})

def eliminar(request, id):
    categoria = Categoria.objects.get(id=id)
    categoria.delete()
    return render(request, "categorias/lista.html", {"categorias": Categoria.objects.all()})
