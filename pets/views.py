from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductoForm
from .models import Producto
# Create your views here.

def index(request):
    context={}
    return render(request,'pets/index.html',context)

def reg_prod(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tienda')
    else:
        form = ProductoForm()
    return render(request, 'pets/reg_prod.html', {'form': form})

def tienda(request):
    productos = Producto.objects.all()
    return render(request, 'pets/tienda.html', {'productos': productos})

def edit_prod(request):
    producto = get_object_or_404(Producto)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('tienda')
    else:
        form= ProductoForm(instance=producto)
    return render(request, 'pets/edit_prod', {'form': form})