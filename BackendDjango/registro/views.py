from django.http import HttpResponse
from django.shortcuts import render

from registro.models import usuario
#from django.template.loader import get_template

def login(request):
    
    #cargador = get_template('login.html')
    #plantillaLogin=cargador.render()    
    return render(request, "login.html")

def signin(request):
    return render(request, "signin.html")

def buscar(request):
    mensaje="Usuario buscado: %r" %request.GET["nombre"]

    return HttpResponse(mensaje)

def insertar(request):

    mensaje="Usuario buscado: %r" %request.GET["anio"]

    usr = usuario(email = request.GET["correo"], 
        password = request.GET["contrasenia"],
        nombre = request.GET["nombre"],
        apellido = request.GET["apellido"],
        #telefono = request.GET["telefono"],
        fecha_nac = request.GET["anio"] + "-" + request.GET["mes"] + "-" + request.GET["dia"]
    )
    usr.save()

    return render(request, "index.html")

    #request.GET["nombre"]

def contacto(request):

    if request.method == "POST":
        return render(request, "perate.html")

    return render(request, "login.html")

def inicio(request):
    return render(request, "index.html")
