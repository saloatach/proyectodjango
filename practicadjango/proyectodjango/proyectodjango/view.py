from django.http import HttpResponse
from django.template import loader

def home(self,name):
    return HttpResponse (f"Hola soy{name}")

def homepage(self):
    data = {"nombre": "Salomón", "apellido": "Atach"}
    planilla =loader.get_template ("home.html")
    documento= planilla.render (data)
    return HttpResponse (documento)

def curso (self):
    planilla =loader.get_template ("curso.html")
    documento= planilla.render ()
    return HttpResponse (documento)