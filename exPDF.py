from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

cnv = canvas.Canvas('meu_pdf.pdf')
cnv.drawAlignedString(250,450,'Meu primeiro pdf em python')
cnv.save()

