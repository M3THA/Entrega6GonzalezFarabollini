from django.shortcuts import render
#from models import *
from django.http import HttpResponse
from django.template import *
from Familiapp.models import *
# Create your views here.

def familia(self):
    hija= Familia(nombre="Hidalga", apellido="Gonzalez", edad=27, fecha_de_nacimiento="1994-7-4")
    hija.save()
    texto1= f"Datos de hija: {hija.nombre} {hija.apellido}, edad: {hija.edad}, fecha de nacimiento: {hija.fecha_de_nacimiento} <p>"
    
    hijo= Familia(nombre="Pedro", apellido="Gonzalez", edad=28, fecha_de_nacimiento="1993-7-5")
    hijo.save()
    texto2= f"Datos de hijo: {hijo.nombre} {hijo.apellido}, edad: {hijo.edad}, fecha de nacimiento: {hijo.fecha_de_nacimiento}</p>"

    padre= Familia(nombre="Alfonzo", apellido="Gonzalez", edad=57, fecha_de_nacimiento="1965-9-3")
    padre.save()
    texto3= f"Datos de padre: {padre.nombre} {padre.apellido}, edad: {padre.edad}, fecha de nacimiento: {padre.fecha_de_nacimiento}<p>"

    madre= Familia(nombre="Veronica", apellido="Litch", edad=56, fecha_de_nacimiento="1966-9-14")
    madre.save()
    texto4= f"Datos de madre: {madre.nombre} {madre.apellido}, edad: {madre.edad}, fecha de nacimiento: {madre.fecha_de_nacimiento}</p>"


    texto_final=  (texto1+texto2+texto3+texto4)

    return HttpResponse(texto_final)
