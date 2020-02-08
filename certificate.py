from PyPDF2 import PdfFileWriter, PdfFileReader
import io

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Adding custom fonts. 1st parm is the name of the font and 2nd is the path to the ttf font file.
pdfmetrics.registerFont(TTFont('Roboto', 'RobotoMono-Medium.ttf'))
pdfmetrics.registerFont(TTFont('RobotoL', 'RobotoMono-Light.ttf'))


# Function to return a pdf page with the parameters added into it.
def createpage(name):
    packet = io.BytesIO()
    can = canvas.Canvas(packet)
    
    can.setFont('Roboto', 17)

    # You'll have to determine the following values with the help of the helper file, get_pdf_coordinates.py
    start = 40
    end = 810
    length_of_one_letter = 10               # Use some 'monospaced' font so that each letter will have the same length.
    y = 310

    mid = start + (end - start)/2
    half_string_size = (len(name)/2)*length_of_one_letter
    x = mid - half_string_size
    can.drawString(x, y, name)
    # =======================================================================================================
    

    can.save()                               # Save the canvas


    packet.seek(0)
    # Creating a pdf with just the canvas we just created.
    new_pdf = PdfFileReader(packet)

    # Read your existing PDF (ticket.pdf)
    existing_pdf = PdfFileReader(open("Auto360.pdf", "rb")) # add blank workshop pdf here
    # Add the canvas on the existing page
    page = existing_pdf.getPage(0)
    page2 = new_pdf.getPage(0)
    page.mergePage(page2)

    return page


#############################################################################

names = [] # add list of names 

import json

if __name__=="__main__":
 
    for name in new_names:
        name = name.upper()

        output = PdfFileWriter()

        page = createpage(name)
        output.addPage(page)

        outputStream = open('cert3/'+name+".pdf", "wb")
        output.write(outputStream)
        outputStream.close()
        print('certificate generated for ' + name)

