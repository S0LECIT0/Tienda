from django.shortcuts import render
from .models import Categoria

# Crear
def crear(request):
    if request.method == "POST":
        categoria = Categoria(
            nombre=request.POST["nombre"],
            observaciones=request.POST["observaciones"]
        )
        categoria.save()
    return render(request, "categorias/formulario.html")

# Listar
def listar(request):
    categorias = Categoria.objects.all()
    return render(request, "categorias/lista.html", {"categorias": categorias})

# Ver
def detalle(request, id):
    categoria = Categoria.objects.get(id=id)
    return render(request, "categorias/detalle.html", {"categoria": categoria})

# Editar
def editar(request, id):
    categoria = Categoria.objects.get(id=id)

    if request.method == "POST":
        categoria.nombre = request.POST["nombre"]
        categoria.observaciones = request.POST["observaciones"]
        categoria.save()
        return render(request, "categorias/detalle.html", {"categoria": categoria})

    return render(request, "categorias/formulario.html", {"categoria": categoria})

# Eliminar
def eliminar(request, id):
    categoria = Categoria.objects.get(id=id)
    categoria.delete()
    return render(request, "categorias/lista.html", {"categorias": Categoria.objects.all()})