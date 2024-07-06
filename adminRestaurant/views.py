from django.shortcuts import render
from .models import Ingrediente, Empleado, Gasto

# Views para Inventario

def inventario(request):
    ingredientes = Ingrediente.objects.all()
    context = {'ingredientes': ingredientes}
    return render(request, 'adminRestaurant/inventario_list.html', context)

def inventarioAdd(request):
    if request.method != "POST":
        context = {}  # Puedes añadir más contexto si es necesario
        return render(request, 'adminRestaurant/inventario_add.html', context)
    else:
        # Procesar los datos del formulario y guardar en la base de datos
        id_ingrediente = request.POST["id_ingrediente"]
        costo_ingrediente = request.POST["costo_ingrediente"]
        costo_mensual = request.POST["costo_mensual"]

        ingrediente = Ingrediente.objects.create(
            id_ingredientes=id_ingrediente,
            costo_ingrediente=costo_ingrediente,
            costo_mensual=costo_mensual
        )

        context = {'mensaje': 'Datos de inventario grabados correctamente.'}
        return render(request, 'adminRestaurant/inventario_add.html', context)

def inventarioDel(request, pk):
    try:
        ingrediente = Ingrediente.objects.get(id_ingredientes=pk)
        ingrediente.delete()
        mensaje = "Datos de inventario eliminados correctamente."
    except Ingrediente.DoesNotExist:
        mensaje = "Error, el ingrediente no existe."

    ingredientes = Ingrediente.objects.all()
    context = {'ingredientes': ingredientes, 'mensaje': mensaje}
    return render(request, 'adminRestaurant/inventario_list.html', context)

def inventarioEdit(request, pk):
    try:
        ingrediente = Ingrediente.objects.get(id_ingredientes=pk)
        context = {'ingrediente': ingrediente}
        return render(request, 'adminRestaurant/inventario_edit.html', context)
    except Ingrediente.DoesNotExist:
        context = {'mensaje': "Error, ingrediente no encontrado."}
        return render(request, 'adminRestaurant/inventario_list.html', context)

def inventarioUpdate(request):
    if request.method == "POST":
        id_ingrediente = request.POST["id_ingrediente"]
        costo_ingrediente = request.POST["costo_ingrediente"]
        costo_mensual = request.POST["costo_mensual"]

        try:
            ingrediente = Ingrediente.objects.get(id_ingredientes=id_ingrediente)
            ingrediente.costo_ingrediente = costo_ingrediente
            ingrediente.costo_mensual = costo_mensual
            ingrediente.save()
            mensaje = "Datos de inventario actualizados correctamente."
        except Ingrediente.DoesNotExist:
            mensaje = "Error, ingrediente no encontrado."

        ingredientes = Ingrediente.objects.all()
        context = {'ingredientes': ingredientes, 'mensaje': mensaje}
        return render(request, 'adminRestaurant/inventario_list.html', context)
    else:
        ingredientes = Ingrediente.objects.all()
        context = {'ingredientes': ingredientes}
        return render(request, 'adminRestaurant/inventario_list.html', context)


# Views para Empleados

def empleados(request):
    empleados = Empleado.objects.all()
    context = {'empleados': empleados}
    return render(request, 'adminRestaurant/empleados_list.html', context)

def empleadosAdd(request):
    if request.method != "POST":
        context = {}  # Puedes añadir más contexto si es necesario
        return render(request, 'adminRestaurant/empleados_add.html', context)
    else:
        # Procesar los datos del formulario y guardar en la base de datos
        id_empleado = request.POST["id_empleado"]
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        labor = request.POST["labor"]

        empleado = Empleado.objects.create(
            id_empleados=id_empleado,
            nombre=nombre,
            apellido=apellido,
            labor=labor
        )

        context = {'mensaje': 'Datos de empleado grabados correctamente.'}
        return render(request, 'adminRestaurant/empleados_add.html', context)

def empleadosDel(request, pk):
    try:
        empleado = Empleado.objects.get(id_empleados=pk)
        empleado.delete()
        mensaje = "Datos de empleado eliminados correctamente."
    except Empleado.DoesNotExist:
        mensaje = "Error, el empleado no existe."

    empleados = Empleado.objects.all()
    context = {'empleados': empleados, 'mensaje': mensaje}
    return render(request, 'adminRestaurant/empleados_list.html', context)

def empleadosEdit(request, pk):
    try:
        empleado = Empleado.objects.get(id_empleados=pk)
        context = {'empleado': empleado}
        return render(request, 'adminRestaurant/empleados_edit.html', context)
    except Empleado.DoesNotExist:
        context = {'mensaje': "Error, empleado no encontrado."}
        return render(request, 'adminRestaurant/empleados_list.html', context)

def empleadosUpdate(request):
    if request.method == "POST":
        id_empleado = request.POST["id_empleado"]
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        labor = request.POST["labor"]

        try:
            empleado = Empleado.objects.get(id_empleados=id_empleado)
            empleado.nombre = nombre
            empleado.apellido = apellido
            empleado.labor = labor
            empleado.save()
            mensaje = "Datos de empleado actualizados correctamente."
        except Empleado.DoesNotExist:
            mensaje = "Error, empleado no encontrado."

        empleados = Empleado.objects.all()
        context = {'empleados': empleados, 'mensaje': mensaje}
        return render(request, 'adminRestaurant/empleados_list.html', context)
    else:
        empleados = Empleado.objects.all()
        context = {'empleados': empleados}
        return render(request, 'adminRestaurant/empleados_list.html', context)


# Views para Gastos

def gastos(request):
    gastos = Gasto.objects.all()
    context = {'gastos': gastos}
    return render(request, 'adminRestaurant/gastos_list.html', context)

def gastosAdd(request):
    if request.method != "POST":
        context = {}  # Puedes añadir más contexto si es necesario
        return render(request, 'adminRestaurant/gastos_add.html', context)
    else:
        # Procesar los datos del formulario y guardar en la base de datos
        costo_total = request.POST["costo_total"]
        liquidaciones = request.POST["liquidaciones"]
        costo_mensual = request.POST["costo_mensual"]
        arriendo_local = request.POST["arriendo_local"]

        gasto = Gasto.objects.create(
            costo_total=costo_total,
            liquidaciones=liquidaciones,
            costo_mensual=costo_mensual,
            arriendo_local=arriendo_local
        )

        context = {'mensaje': 'Datos de gasto grabados correctamente.'}
        return render(request, 'adminRestaurant/gastos_add.html', context)

def gastosDel(request, pk):
    try:
        gasto = Gasto.objects.get(costo_total=pk)
        gasto.delete()
        mensaje = "Datos de gasto eliminados correctamente."
    except Gasto.DoesNotExist:
        mensaje = "Error, el gasto no existe."

    gastos = Gasto.objects.all()
    context = {'gastos': gastos, 'mensaje': mensaje}
    return render(request, 'adminRestaurant/gastos_list.html', context)

def gastosEdit(request, pk):
    try:
        gasto = Gasto.objects.get(costo_total=pk)
        context = {'gasto': gasto}
        return render(request, 'adminRestaurant/gastos_edit.html', context)
    except Gasto.DoesNotExist:
        context = {'mensaje': "Error, gasto no encontrado."}
        return render(request, 'adminRestaurant/gastos_list.html', context)

def gastosUpdate(request):
    if request.method == "POST":
        costo_total = request.POST["costo_total"]
        liquidaciones = request.POST["liquidaciones"]
        costo_mensual = request.POST["costo_mensual"]
        arriendo_local = request.POST["arriendo_local"]

        try:
            gasto = Gasto.objects.get(costo_total=costo_total)
            gasto.liquidaciones = liquidaciones
            gasto.costo_mensual = costo_mensual
            gasto.arriendo_local = arriendo_local
            gasto.save()
            mensaje = "Datos de gasto actualizados correctamente."
        except Gasto.DoesNotExist:
            mensaje = "Error, gasto no encontrado."

        gastos = Gasto.objects.all()
        context = {'gastos': gastos, 'mensaje': mensaje}
        return render(request, 'adminRestaurant/gastos_list.html', context)
    else:
        gastos = Gasto.objects.all()
        context = {'gastos': gastos}
        return render(request, 'adminRestaurant/gastos_list.html', context)
