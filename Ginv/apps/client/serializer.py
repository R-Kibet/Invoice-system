from rest_framework import serializers
from .models import Client

# main function of serializer -> get info from db and convert to json

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        read_only_fields = (
            "created_at",
            "created_by"
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

        )