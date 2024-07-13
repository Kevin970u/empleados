from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Categoria, Empresa, Costo


# funciones del modelo Categoria
def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'listar_categorias.html', {'categorias': categorias})

def crear_categoria(request):
    if request.method == 'POST':
        categoria_cat = request.POST['categoria_cat']
        Categoria.objects.create(categoria_cat=categoria_cat)
        return redirect('/')
    return render(request, 'crear_categoria.html')

def editar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.categoria_cat = request.POST['categoria_cat']
        categoria.save()
        return redirect('/')
    return render(request, 'editar_categoria.html', {'categoria': categoria})

def eliminar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        return JsonResponse({'message': 'Categoria eliminada correctamente.'})
    return JsonResponse({'error': 'No se pudo eliminar la categoría.'}, status=400)

# funciones del modelo Empresa

def listar_empresas(request):
    empresas = Empresa.objects.all()
    return render(request, 'listar_empresas.html', {'empresas': empresas})

def crear_empresa(request):
    if request.method == 'POST':
        empresa_empre = request.POST['empresa_empre']
        Empresa.objects.create(empresa_empre=empresa_empre)
        return redirect('listar_empresas')
    return render(request, 'crear_empresa.html')

def editar_empresa(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    if request.method == 'POST':
        empresa.empresa_empre = request.POST['empresa_empre']
        empresa.save()
        return redirect('listar_empresas')
    return render(request, 'editar_empresa.html', {'empresa': empresa})

def eliminar_empresa(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    if request.method == 'POST':
        empresa.delete()
        return JsonResponse({'message': 'Empresa eliminada correctamente.'})
    return JsonResponse({'error': 'No se pudo eliminar la empresa.'}, status=400)

# Funciones del modelo Costo

def listar_costos(request):
    costos = Costo.objects.all()
    return render(request, 'listar_costos.html', {'costos': costos})

def crear_costo(request):
    if request.method == 'POST':
        c_costo_cos = request.POST['c_costo_cos']
        Costo.objects.create(c_costo_cos=c_costo_cos)
        return redirect('listar_costos')
    return render(request, 'crear_costo.html')

def editar_costo(request, pk):
    costo = get_object_or_404(Costo, pk=pk)
    if request.method == 'POST':
        costo.c_costo_cos = request.POST['c_costo_cos']
        costo.save()
        return redirect('listar_costos')
    return render(request, 'editar_costo.html', {'costo': costo})

def eliminar_costo(request, pk):
    costo = get_object_or_404(Costo, pk=pk)
    if request.method == 'POST':
        costo.delete()
        return JsonResponse({'message': 'Costo eliminado correctamente.'})
    return JsonResponse({'error': 'No se pudo eliminar el costo.'}, status=400)