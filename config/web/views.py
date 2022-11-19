from django.shortcuts import render
from web.formularios.formularioPlatos import FormularioRegistroPlatos
from web.formularios.formularioEmpleados import FormularioEmpleados
from web.models import Platos
from web.models import Empleados

# Create your views here.

#CADA VISTA ES UNA FUNCION DE PY

def Home(request):
    return render(request,'index.html')

def PlatosVista(request):

    #CARGAR FORMULARIO DE REGISTRO DE PLATOS
    formulario = FormularioRegistroPlatos()

    #creamos un diccionario para enviar datos hacia el template
    diccionarioEnvio = {
        'formul': formulario
    }

    #recibiendo datos del formulario 
    # PETICION DE TIPO POST

    if request.method == 'POST':
        datosFormulario = FormularioRegistroPlatos(request.POST)
        if datosFormulario.is_valid():
            datosLimpios =datosFormulario.cleaned_data
            #enviando datos a mi base de datos
            platonuevo = Platos(
                nombre = datosLimpios["nombrePlato"],
                descripcion= datosLimpios["descripcionPlato"],
                imagen = datosLimpios["fotoPlato"],
                precio = datosLimpios["precioPlato"],
                tipo = datosLimpios["tipoPlato"]
            )
            platonuevo.save()





    return render(request,'platos.html',diccionarioEnvio)
    

def EmpleadosVista(request):

         #CARGAR FORMULARIO DE REGISTRO DE PLATOS
        formularioempl = FormularioEmpleados()

        #creamos un diccionario para enviar datos hacia el template
        diccionarioEmpl = {
            'emple': formularioempl
        }

        #recibiendo datos del formulario 
        # PETICION DE TIPO POST

        if request.method == 'POST':
            datosForm = FormularioEmpleados(request.POST)
            if datosForm.is_valid():
                datosLimp =datosForm.cleaned_data
                empleadonuevo = Empleados(
                   
                    tipodoc = datosLimp["tipoDoc"],
                    numerodoc= datosLimp["numeroDocumento"],
                    nombreempleado = datosLimp["nombreEmpleado"],
                    telefonoempl = datosLimp["telefonoEmpleado"],
                    correoemp = datosLimp["correoEmpleado"]
            )
            empleadonuevo.save()


        return render(request,'empleados.html',diccionarioEmpl)
        

        #CARGAR FORMULARIO DE REGISTRO DE PLATOS
