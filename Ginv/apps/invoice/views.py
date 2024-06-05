import pdfkit

from django.core.exceptions import PermissionDenied
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import get_template

from rest_framework import viewsets 
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from .models import Invoice, Item
from .serializer import InvoiceSerializer, ItemSerializer

from apps.team.models import Team


class InvoiceViewset(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()


    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)
    

    def perform_create(self, serializer):
        team = self.request.user.teams.first()
        invoice_num = team.invoice_1
        team.invoice_1 = invoice_num + 1
        team.save()

        serializer.save(created_by=self.request.user, team=team, modified_by=self.request.user, invoice_no=invoice_num, bankaccount=team.bankaccount )


    def perform_update(self, serializer):
        obj = self.get_object()

        if self.request.user != obj.created_by:
            raise PermissionDenied("Wrong object user")
        
        serializer.save()


@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def generate_pdf(request, invoice_id):

    invoice = get_object_or_404(Invoice, pk=invoice_id, created_by=request.user)
    team = Team.objects.filter(created_by=request.user).first()

    if invoice.is_credited:
        template_name = 'pdf_credit.html'
    else:
        template_name = 'pdf.html'

    template = get_template(template_name)
    html = template.render({'invoice': invoice, 'team': team})
    pdf = pdfkit.from_string(html, False, options={})

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment: filename="invoice.pdf"'

    return response


@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def send_reminder(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id, created_by=request.user)  
    team = Team.objects.filter(created_by=request.user).first()

    subject = 'Unpaid Invoices'
    from_email = team.email
    to = [invoice.client.email]
    text_content = f"You have an unpaid invoice. Invoice number: #' {invoice.invoice_no}"
    html_content = f"You have an unpaid invoice. Invoice number: #' {invoice.invoice_no}"

    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")


    template = get_template('pdf.html')
    html = template.render({'invoice': invoice, 'team': team})
    pdf = pdfkit.from_string(html, False, options={})


    if pdf:
        name = 'invoice_%s.pdf' % invoice.invoice_no
        msg.attach(name, pdf, 'application/pdf')

    msg.send()
    
    return Response()