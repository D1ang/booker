from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import datetime
from weasyprint import HTML


def generate_quotation(request: HttpRequest) -> HttpResponse:
    """Generate a quotation PDF and render the quotation template."""
    today = datetime.now(tz=datetime.timezone.utc).strftime('%B %-d, %Y')

    context = {'date': today}
    rendered = render(request, 'invoice/invoice.html', context)

    html = HTML(string=rendered)
    rendered_pdf = html.write_pdf('./static/invoice.pdf')

    return render(request, 'invoice/invoice.html', context)
