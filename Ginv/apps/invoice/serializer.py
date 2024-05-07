from rest_framework import serializers
from .models import Invoice, Item

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        read_only_fields = (
            "team",
            "created_at",
            "created_by",
            "modified_at",
            "modified_by"
        ),
        fields = (
            "id",
            "client",
            "client_name",
            "client_email"
            "client_org_id",
            "client_add1",
            "client_add2",
            "client_zipcd",
            "client_place",
            "client_country",
            "client_contact",
            "client_contact_ref",
            "sender_ref",
            "invoice_type",
            "due_days",
            "is_sent",
            "gross_amount",
            "vat_amount",
            "net_amount",
            "discount_amount"




        )

