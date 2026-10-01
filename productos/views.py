from django.shortcuts import render
from .models import Producto

def crear(request):
    if request.method == "POST":
        producto = Producto(
            nombre=request.POST["nombre"],
            categoria=request.POST["categoria"],
            precio=request.POST["precio"],
            cantidad=request.POST["cantidad"],
            estado=request.POST.get("estado") == "on"
        )

        producto.save()
    
    return render(request, "productos/formulario.html")

def listar(request):
    productos = Producto.objects.all()

    return render(request, "productos/lista.html", {"productos": productos})

def detalle(request, id):
    producto = Producto.objects.get(id=id)

    return render(request, "productos/detalle.html", {"producto": producto})

def editar(request, id):
    producto = Producto.objects.get(id=id)

    if request.method == "POST":
        producto.nombre = request.POST["nombre"]
        producto.categoria = request.POST["categoria"]
        producto.precio = request.POST["precio"]
        producto.cantidad = request.POST["cantidad"]
        producto.estado = request.POST["estado"]
        producto.estado = request.POST.get("estado") == "on"

        producto.save()

        return render(request, "productos/detalle.html", {"producto": producto})

    return render(request, "productos/formulario.html", {"producto": producto})

def eliminar(request, id):
    producto = Producto.objects.get(id=id)

    producto.delete()

    return render(request, "productos/lista.html", {"productos": Producto.objects.all()})
