from django.shortcuts import render
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
import datetime

def registroPdf(request, queryset):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.setLineWidth(.3)
    today = datetime.date.today()
    solicitador = "Mr. Krabs"

    p.drawString(220, 800, "Registro del "+str(today))
    p.drawString(30, 770,"Solicitado por: "+solicitador)
    y = 750
    for i in queryset.order_by('id'):
        p.drawString(30, y, "•"+"Registro "+str(i.id))
        y -= 15
        p.drawString(40, y, "Fecha: "+str(i.fecha))
        y -= 15
        p.drawString(40, y, "Descripcion: "+str(i.descripcion))
        y -= 15
        p.drawString(40, y, "Usuario: "+str(i.usuario))
        y -= 20

    p.showPage()
    p.save()

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=False, filename='registro.pdf')

def objetoPdf(request, queryset):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.setLineWidth(.3)
    today = datetime.date.today()
    w = 750
    p.drawString(220, 800, "Stock del "+str(today))
    p.drawString(30, 770,"Solicitado por: ")

    for i in queryset.order_by('conjunto'):

        p.drawString(30, w, "Conjunto: "+str(i.conjunto))
        w -= 15
        for i in queryset:
            if (w <= 100):
                p.showPage()
                w = 750
            p.drawString(40, w, "Objeto: "+str(i.id_Colegio))
            w -= 15
            p.drawString(50, w, "Modelo: "+str(i.modelo))
            w -= 15
            p.drawString(50, w, "Marca: "+str(i.marca))
            w -= 15
            estado = ""
            if(i.estado == 1):
                estado = "Disponible"
            elif(i.estado == 2):
                estado = "Prestado"
            elif(i.estado == 3):
                estado = "En mantenimiento"
            p.drawString(50, w, "Estado: "+estado)
            w -= 15
            condicion = ""
            if(i.condicion == 1):
                condicion = "Nuevo"
            elif(i.condicion == 2):
                condicion = "Usado"
            elif(i.condicion == 3):
                condicion = "Arreglar"
            elif(i.condicion == 4):
                condicion = "Roto"
            p.drawString(50, w, "Condicion: "+condicion)
            w -= 15
            p.drawString(50, w, "Descripcion: "+str(i.descripcion))
            w -= 20








    p.showPage()
    p.save()

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=False, filename='objeto.pdf')
