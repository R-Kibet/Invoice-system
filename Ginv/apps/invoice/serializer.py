from rest_framework import serializers
from .models import Invoice, Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        read_only_fields = (
            "invoice",
        )
        fields = (
            "id",
            "title",
            "quantity",
            "unit_price",
            "net_amount",
            "vat_rate",
            "discount"
        )


class InvoiceSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    bankaccount = serializers.CharField(required=False)

    class Meta:
        model = Invoice
        read_only_fields = (
            "team",
            "created_at",
            "created_by",
            "modified_at",
            "invoice_no",
            "modified_by"
        ),
        fields = (
            "id",
            "invoice_no",
            "client",
            "client_name",
            "client_email",
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
            "discount_amount",
            "is_paid",
            "bankaccount",
            "items"
        )

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        invoice = Invoice.objects.create(**validated_data)

        for item in items_data:
            Item.objects.create(invoice=invoice, **item)

        return invoice
