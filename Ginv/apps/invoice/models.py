from django.contrib.auth.models import User
from django.db import models

from apps.client.models import Client
from apps.team.models import Team

class Invoice(models.Model):
    INVOICE = 'invoice'
    CREDIT_NOTE = 'credit_note'

    CHOICES_TYPE = (
        (INVOICE, "Invoice"),
        (CREDIT_NOTE, "Credit note")
    )  

    invoice_no  = models.IntegerField(default=1)
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    client_org_id = models.CharField(max_length=100, blank=True, null=True)
    client_add1 = models.CharField(max_length=100, blank=True, null=True)
    client_add2 = models.CharField(max_length=100, blank=True, null=True)
    client_zipcd = models.CharField(max_length=100, blank=True, null=True)
    client_place = models.CharField(max_length=100, blank=True, null=True)
    client_country = models.CharField(max_length=100, blank=True, null=True)
    client_contact = models.CharField(max_length=100, blank=True, null=True)
    client_contact_ref = models.CharField(max_length=100, blank=True, null=True)
    sender_ref = models.CharField(max_length=100, blank=True, null=True)
    invoice_type = models.CharField(max_length=20, choices=CHOICES_TYPE, default=INVOICE)
    due_days = models.IntegerField(default=14)
    is_credit_for = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    is_sent = models.BooleanField(default=False)
    gross_amount = models.DecimalField(max_digits=7, decimal_places=2)
    vat_amount = models.DecimalField(max_digits=6, decimal_places=2)
    net_amount = models.DecimalField(max_digits=7, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=6, decimal_places=2)
    team = models.ForeignKey(Team, related_name='invoices', on_delete=models.CASCADE)
    client = models.ForeignKey(Client, related_name='invoices', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name="created_invoices", on_delete=models.CASCADE)
    modified_by = models.ForeignKey(User, related_name='modified_invoices', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.client_name
    
class Item(models.Model):
    invoice = models.ForeignKey(Invoice, related_name="items", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    unit_price = models.DecimalField(max_digits=7, decimal_places=2)
    net_amount = models.DecimalField(max_digits=7, decimal_places=2)
    vat_rate = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
