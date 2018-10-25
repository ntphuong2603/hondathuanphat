from django.db import models


class ProductCaterogy(models.Model):
    name = models.CharField("Loại xe", max_length=30)
    class Meta:
        db_table = "Caterogy"
