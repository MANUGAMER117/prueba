from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

def lista_productos(request):
    productos = Producto.objects.all()  # Obtiene todos los productos de la base de datos
    return render(request, 'shop/lista_productos.html', {'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
        
    else:
        form = ProductoForm()
        return render(request, 'shop/agregar_producto.html', {'form': form})
    
def agregar_al_carrito(request, producto_id):
    carrito_id = request.session.get('carrito_id')
    carrito, created = Carrito.objects.get_or_create(id = carrito_id)
    if cretaed:
        request.session['carrito_id'] = carrito.id
        producto = get_object_or_404(Producto, id = producto_id)
    carrito_producto, created = CarritoProducto.objects.get_or_create(carrito = carrito, producto = producto)
    if not created:
        carrito_producto.cantidad += 1
    carrito_producto.save()
    return redirect('lista_productos')

def proceso_compra(request):
    carrito_id = request.session.get('carrito_id')
    carrito = get_object_or_404(Carrito, id=carrito_id)
    carrito_productos = carrito.carritoproducto_set.all()

    if request.method == 'POST':
        carrito.delete()
        del request.session['carrito_id']
        return redirect('lista_productos')
    
    return render(request, 'shop/proceso_compra.html', {'carrito_productos': carrito_productos})