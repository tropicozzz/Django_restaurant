from django.shortcuts import render

# Create your views here.
def inicio(request):

    return render(request,'adminRestaurant/inicio.html')

def gastos(request):

    return render(request,'adminRestaurant/gastos.html')

def index(request):

    return render(request,'adminRestaurant/index.html')

def empleados(request):

    return render(request,'adminRestaurant/empleados.html')

def inventario(request):

    return render(request,'adminRestaurant/inventario.html')