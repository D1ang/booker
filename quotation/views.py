from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import datetime
from weasyprint import HTML
from .models import Quotation


def generate_quotation(request: HttpRequest) -> HttpResponse:
    """Generate a quotation PDF and render the quotation template."""
    # today = datetime.now(tz=datetime.timezone.utc).strftime('%B %-d, %Y')



    today = datetime.now().strftime('%B %-d, %Y')

    context = {'date': today}
    # rendered = render(request, 'invoice/invoice.html')

    # html = HTML(string=rendered)
    # rendered_pdf = html.write_pdf('./static/invoice.pdf')

    return render(request, 'quotation/quotation.html', context)


def quotation_details(request, quotation_number):
    """Render the quotation details page."""
    quotation = Quotation.objects.get(quotation_number=quotation_number)
    quotation_rules = quotation.quotationrule_set.all()


    print(quotation_rules)

    for rule in quotation_rules:
        print(rule.description, rule.amount)

    context = {
        'quotation': quotation,
        'quotation_rules': quotation_rules,
    }

    return render(request, 'quotation/details.html', context)
