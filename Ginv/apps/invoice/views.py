from .models import Invoice, Item
from .serializer import InvoiceSerializer, ItemSerializer

from rest_framework import viewsets

from django.core.exceptions import PermissionDenied


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


