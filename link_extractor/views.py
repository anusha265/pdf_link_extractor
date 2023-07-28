from django.shortcuts import render
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import PyPDF2
def extract_links(request):
    if request.method == 'POST':
        pdf_file = request.FILES['pdf_file']
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        links = []
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            if '/Annots' in page:
                annotations = page['/Annots']
                if annotations:
                    for annotation in annotations:
                        annotation = annotation.get_object()
                        if '/Subtype' in annotation and annotation['/Subtype'] == '/Link':
                            if '/A' in annotation and '/URI' in annotation['/A']:
                                link = annotation['/A']['/URI']
                                links.append(link)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="extracted_links.pdf"'
        c = canvas.Canvas(response, pagesize=letter)
        c.setFont("Helvetica", 12)
        for index, link in enumerate(links):
            c.drawString(50, 750 - (index * 20), link)
        c.showPage()
        c.save()
        return response
    elif request.method == 'GET':
        return render(request, 'link_extractor/extract_links.html')
    return HttpResponse(status=405)

