from rest_framework import serializers
from .models import Client
from apps.invoice.models import Invoice # type: ignore

# main function of serializer -> get info from db and convert to json

class ClientInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = (
            "id",
            "invoice_no",
            "is_sent",
            "is_paid",
            "gross_amount",
            "vat_amount",
            "net_amount",
            "get_due_date_formatted",
            "invoice_type",
            "is_credited"
        )


class ClientSerializer(serializers.ModelSerializer):
    invoices = ClientInvoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Client

        read_only_fields = (
            "created_at",
            "created_by",
        ),

        fields = (
            "id",
            "name",
            "email",
            "org_id",
            "address",
            "add2",
            "zipcd",
            "place",
            "country",
            "contact",
            "contact_ref",
            "invoices",

        )

    