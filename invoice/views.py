from django.shortcuts import render
from datetime import datetime
from weasyprint import HTML


def generate_invoice(request):
    """
    A view that displays the index page and renders
    the three most clicked services.
    """
    today = datetime.today().strftime("%B %-d, %Y")
    # html = HTML('/templates/invoice/invoice.html')
    # html.write_pdf('invoice.pdf')

    context = {'date': today}
    
    rendered = render(request, 'invoice/invoice.html', context)
    print(rendered)




    
    html = HTML(string=rendered)
    rendered_pdf = html.write_pdf('./static/invoice.pdf')




    return render(request, 'invoice/invoice.html', context)
