from django.shortcuts import render
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
import datetime

def registroPdf(request):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.setLineWidth(.3)
    today = datetime.date.today()
    solicitador = "Mr. Krabs"

    p.drawString(220, 800, "Registro del "+str(today))
    p.drawString(30, 770,"Solicitado por: "+solicitador)
    y = 750
    for i in range(6):

        p.drawString(30, y, "•"+"Esto va asi por ahora gente")
        y -=20


    p.showPage()
    p.save()

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=False, filename='registro.pdf')
