from django.contrib.auth.models import User
from django.db import models



class Team(models.Model):
    name = models.CharField(max_length=100)
    org_id = models.CharField(max_length=100, blank=True, null=True)
    invoice_1 = models.IntegerField(default=1)
    created_by = models.ForeignKey(User, related_name='teams', on_delete=models.CASCADE)
    bankaccount = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

